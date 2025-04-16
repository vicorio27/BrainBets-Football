import requests


def get(url: str, query_params: dict):
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers, params=query_params)
    return response


def post(url: str, payload: dict):
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=payload)
    return response
