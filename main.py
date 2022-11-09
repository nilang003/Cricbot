import telebot
import requests
from app import cricFuntionality
bot = telebot.TeleBot("5797737730:AAGLdTGW6wiLIlM-EvYGOynNg6cu6-Tj_-A")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")



@bot.message_handler(commands=['test'])
def send_key(message):
    r=requests.get("https://unofficial-cricbuzz.p.rapidapi.com/matches/list?matchState=live",headers={
    "X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com",
    "X-RapidAPI-Key": "7d3a4d6461mshdd4d2d19f04bba3p1f2b7djsna1fd1e286dff"
})
    resp=r.json()
    internationalMatches=resp["typeMatches"][0]["seriesAdWrapper"]
    for match in internationalMatches:
        try:
            # print(match["seriesMatches"]["seriesName"],match["seriesMatches"]["matches"])
            matches = match["seriesMatches"]["matches"]
            buttons = telebot.types.InlineKeyboardMarkup(row_width=1)
            for i in range(len(matches)):
                text =matches[i]['matchInfo']["team1"]["teamSName"]+ " vs "+ matches[i]['matchInfo']["team2"]["teamSName"]
                # print(text)
                data = str(matches[i]['matchInfo']["matchId"]) + " Live"
                print(data)
                buttons.add(telebot.types.InlineKeyboardButton(text=text, callback_data=data))
            
            chat_id = message.chat.id
            # matchName = match["seriesMatches"]["seriesName"] + " " + match["seriesMatches"]["seriesId"]
            info = "*Select any of the Live match*"
            # bot.send_message(chat_id, info, reply_markup=buttons)
            bot.send_message(chat_id, info, parse_mode='Markdown', reply_markup=buttons)
            # bot.send_message(chat_id,"text",reply_markup=buttons)
        except:
            print("error")
   

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    data = call.data.split(" ");
    print(data)
    matchId = data[0]
    matchStatus = data[1];
    print(matchId, matchStatus)
    if matchStatus == "Live":
        match = cricFuntionality(matchId)
        score = match.getMatchScore()
        print(score)
        if score["isMatchStarted"]:
            if score["isMatchOver"]:
                bot.send_message(call.message.chat.id, score["message"])
            elif not score["isFirstInningsOver"]:
                message = "*"+score["currentBattingTeam"]+"*: "+ str(score["currentScore"]) + " /" + str(score["currentWickets"]) + "( " + str(score["currentOvers"] )+ " Overs" + " )" +" \n"
                for i in score["currentBatsman"]:
                    message += i["name"] + " : " + str(i["runs"] )+ " (" +str( i["balls"] )+ ")\n"
                bot.send_message(call.message.chat.id, message, parse_mode='Markdown')
            else:
                pass

        else:
            bot.reply_to(call.message.chat.id, score["message"])

        # message = "*"+score["currentBattingTeam"]+"*: "+ str(score["currentScore"]) + " /" + str(score["currentWickets"]) + "( " + str(score["currentOvers"] )+ " Overs" + " )" +" \n"
        # for i in score["currentBatsman"]:
        #     message += i["name"] + " : " + str(i["runs"] )+ " (" +str( i["balls"] )+ ")\n"
        # bot.send_message(call.message.chat.id, message, parse_mode='Markdown')

        # photo = open("5322702.jpg", 'rb')
        # bot.send_photo(call.message.chat.id, photo)
#         r=requests.get("https://unofficial-cricbuzz.p.rapidapi.com/matches/list?matchState=live",headers={
#     "X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com",
#     "X-RapidAPI-Key": "7d3a4d6461mshdd4d2d19f04bba3p1f2b7djsna1fd1e286dff"
# })
#     matchInfo=r.json()
#     endTime = matchInfo["endDate"]


#     r=requests.get("https://unofficial-cricbuzz.p.rapidapi.com/matches/get-commentaries?matchId="+matchId,headers={
#     "X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com",
#     "X-RapidAPI-Key": "7d3a4d6461mshdd4d2d19f04bba3p1f2b7djsna1fd1e286dff"
# })
#     resp=r.json()
#     comments = resp["commentary"]
    # for comment in comments:
    #     print(comment["comment"])
    #     bot.send_message(call.message.chat.id, comment["comment"])
    

if __name__ == '__main__':
    bot.polling()
