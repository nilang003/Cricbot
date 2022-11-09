import requests
r=requests.get("https://unofficial-cricbuzz.p.rapidapi.com/matches/list",headers={
    "X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com",
    "X-RapidAPI-Key": "7d3a4d6461mshdd4d2d19f04bba3p1f2b7djsna1fd1e286dff"
})
resp=r.json()
internationalMatches=resp["typeMatches"][0]["seriesAdWrapper"]
# print(internationalMatches)
latestSeries=internationalMatches[0]["seriesMatches"]["matches"]

for match in internationalMatches:
    try:
        print(match["seriesMatches"]["seriesName"],match["seriesMatches"]["seriesId"])
    except:
        pass
    # print(match["seriesUrl"])
for i in range(len(latestSeries)):
    print(latestSeries[i]['matchInfo']["matchId"],latestSeries[i]['matchInfo']["matchDesc"],latestSeries[i]['matchInfo']["team1"])
    # print(i["matchInfo"]["matchId"],i)
    
# print(resp["typeMatches"][0]["seriesAdWrapper"][0]["seriesMatches"]["matches"])

