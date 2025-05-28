import requests
from constant import API_FOOTBALL, CONTENT_TYPE

def get(url: str, **kwargs):
    headers = {
        "x-rapidapi-key": API_FOOTBALL["API_KEY"],
        "x-rapidapi-host": API_FOOTBALL["API_HOST"],
    }
    response = requests.get(API_FOOTBALL["API"] + url, headers=headers, params=kwargs)
    return response.json()

def post(url: str, payload: dict):
    headers = {"Content-Type": CONTENT_TYPE}
    response = requests.post(url, headers=headers, data=payload)
    return response.json()
