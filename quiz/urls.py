from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from . import views



urlpatterns=[
    path('',views.home, name="home"),
    path('result',views.result, name="result"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('exam/<int:cate_id>/',views.exam, name="exam"),
    path('ques/<int:quest_id>/',views.question, name="quest"),
    
]