import json
import requests
from flask import current_app


def translate(text, source_language, dest_language):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = f"source={source_language}&q={text}&target={dest_language}"
    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "8970bcb45fmshb722248cb8bf35bp1ee418jsne692b3f05afb",
        'accept-encoding': "application/gzip",
        'content-type': "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    try:
        text = response.json()['data']['translations'][0]['translatedText']
    except KeyError:
        return 'Error: the translation service filed.'
    if response.status_code != 200:
        return 'Error: the translation service filed.'
    return text
