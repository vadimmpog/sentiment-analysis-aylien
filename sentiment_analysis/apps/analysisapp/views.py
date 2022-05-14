import json
import requests
from django.http import HttpResponse


def analyze(request):
    if request.method == 'POST':

        text_content = json.loads(request.body)['text']

        url = "https://api.meaningcloud.com/sentiment-2.1"

        payload = {
            'key': '7a4b781664d277733ee63d92557c64cc',
            'txt': text_content,
            'lang': 'en',
        }

        response = requests.post(url, data=payload)

        return HttpResponse(response)
    else:
        return None


def history_by_person_id(request):
    return None


def delete(request):
    return None
