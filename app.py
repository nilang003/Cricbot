import requests
import time
class  cricFuntionality():
    def __init__(self,matchId):
        self.baseURL = "https://unofficial-cricbuzz.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com",
            "X-RapidAPI-Key": "7d3a4d6461mshdd4d2d19f04bba3p1f2b7djsna1fd1e286dff"
        }
        self.matchId = matchId
        self.lastHighlightTimeStamp=time.time()
    def getMatchScore(self):
        r=requests.get(self.baseURL+"matches/get-scorecard?matchId="+self.matchId,headers=self.headers)
        update={
            "isMatchOver":False,
            "isMatchStarted":True,
            "isFirstInningsOver":False,
            "data":[],
            "message":""
        }
        resp=r.json()
        if len(resp["scorecard"])==0:
            update["isMatchStarted"]=False
            update["message"]="Match is not started yet"
            return update
        
        elif len(resp["scorecard"])==1:
            score={}
            score["currentScore"] = resp["scorecard"][0]["score"]
            score["currentWickets"] = resp["scorecard"][0]["wickets"]
            score["currentOvers"] = resp["scorecard"][0]["overs"]
            score["currentBattingTeam"] = resp["scorecard"][0]["batTeamSName"]
            score["currentBatsman"] = []
            for i in resp["scorecard"][0]["batsman"]:
                # print(i)
                try:
                    if i["outDec"] == "batting":
                        info={}
                        info["name"] = i["name"]
                        info["runs"] = i["runs"]
                        info["balls"] = i["balls"]
                        score["currentBatsman"].append(info)
                except:
                    pass
            update["data"].append(score)
        else:
            update["isFirstInningsOver"]=True
            try:
                if resp["isMatchComplete"]:
                    update["isMatchOver"]=True
                    update["message"]=resp["status"]
                    return update
            except:
                pass
            
            score={}
            score["currentScore"] = resp["scorecard"][0]["score"]
            score["currentWickets"] = resp["scorecard"][0]["wickets"]
            score["currentOvers"] = resp["scorecard"][0]["overs"]
            score["currentBattingTeam"] = resp["scorecard"][0]["batTeamSName"]
            score["currentBatsman"] = []
            for i in resp["scorecard"][0]["batsman"]:
                # print(i)
                try:
                    if i["outDec"] == "batting":
                        info={}
                        info["name"] = i["name"]
                        info["runs"] = i["runs"]
                        info["balls"] = i["balls"]
                        score["currentBatsman"].append(info)
                except:
                    pass
            update["data"].append(score)
            score={}
            score["currentScore"] = resp["scorecard"][1]["score"]
            score["currentWickets"] = resp["scorecard"][1]["wickets"]
            score["currentOvers"] = resp["scorecard"][1]["overs"]
            score["currentBattingTeam"] = resp["scorecard"][1]["batTeamSName"]
            score["currentBatsman"] = []
            for i in resp["scorecard"][1]["batsman"]:
                # print(i)
                try:
                    if i["outDec"] == "batting":
                        info={}
                        info["name"] = i["name"]
                        info["runs"] = i["runs"]
                        info["balls"] = i["balls"]
                        score["currentBatsman"].append(info)
                except:
                    pass
            update["data"].append(score)
            

                    

        return update
        
           
