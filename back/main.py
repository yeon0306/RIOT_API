from typing import Union
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # cookie 포함 여부를 설정한다. 기본은 False
    allow_methods=["*"],    # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다.
    allow_headers=["*"],	# 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.
)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-57d2ff9c-8b8c-4f69-b84e-f8b2e1c3c069"
    }

@app.get("/")
def read_root():
    r = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/hide%20on%20bush", headers=header)
    return {"r": r.json()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/getSummonerInfo/{summonerName}")
def get_summoner_info(summonerName: str):
    r = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName, headers=header)
    return {"r": r.json()}

@app.get("/getLeagueInfo/{summonerId}")
def get_league_info(summonerId: str):
    r = requests.get("https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+summonerId, headers=header)
    return r.json()

@app.get("/getMatchList/{summonerPuuid}/{count}")
def get_Match_List(summonerPuuid: str, count: int):
    r = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
                     +summonerPuuid+"/ids?start=0&count="+str(count), headers=header)
    return r.json()

@app.get("/getMatchInfo/{matchId}")
def get_Match_info(matchId: str):
    r = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/"+matchId, headers=header)
    return r.json()
