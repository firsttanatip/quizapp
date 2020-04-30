from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('register',views.register, name="register"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
]