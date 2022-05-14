from django.urls import re_path
from sentiment_analysis.apps.analysisapp import views as analysisapp

app_name = 'analysisapp'

urlpatterns = [
    re_path(r'^analyze/$', analysisapp.analyze, name='analyze'),
    re_path(r'^history/$', analysisapp.history_by_person_id, name='history'),
    re_path(r'^delete/$', analysisapp.analyze, name='analyze'),
]
