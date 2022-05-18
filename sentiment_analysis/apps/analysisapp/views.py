import json
import os

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sentiment_analysis.apps.analysisapp.models import Analysis


def analyze(request):
    save_flag = request.GET.get('save')
    if request.method == 'POST':

        text_content = json.loads(request.body)['text']

        url = "https://api.meaningcloud.com/sentiment-2.1"

        payload = {
            'key': os.environ.get('API_KEY'),
            'txt': text_content,
            'lang': 'en',
        }

        response = requests.post(url, data=payload)

        if save_flag == 'true':
            save({"res": response.json(), "user_id": request.user.id, "text": text_content})

        return HttpResponse(response)
    else:
        return None


def history_by_person_id(request):
    if request.user.is_authenticated:
        objs = Analysis.objects.all().filter(user_id=request.user.id)
        history_list = []
        for analysis in objs:
            history_list.append({
                "id": analysis.id,
                "text": analysis.text,
                "score_tag": analysis.score_tag,
                "irony": analysis.irony,
                "confidence": analysis.confidence
            })
        return HttpResponse(json.dumps(history_list))
    else:
        return redirect('auth:login')


def save(data):
    an = Analysis(user_id=data["user_id"], text=data["text"],
                  score_tag=data["res"]["score_tag"], irony=data["res"]["irony"],
                  confidence=data["res"]["confidence"])
    an.save()


def delete(request):
    hist_id = request.GET.get('hist_id')
    Analysis.objects.get(id=hist_id).delete()
    return HttpResponse("success")


