from django.urls import re_path

import sentiment_analysis.apps.authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path(r'^login/$', authapp.login_request, name='login'),
    re_path(r'^logout/$', authapp.logout, name='logout'),
    re_path(r'^register/$', authapp.register, name='register'),
    # re_path(r'^edit/$', authapp.edit, name='edit'),
    # re_path(r'^personal_data/$', authapp.personal_data, name='personal_data')
]