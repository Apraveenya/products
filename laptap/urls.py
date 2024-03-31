from django.urls import path
from laptap.views import *
appname='laptap'
urlpatterns=[
    path('hp/',hp,name='hp'),
]