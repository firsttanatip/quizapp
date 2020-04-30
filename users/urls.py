from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'
urlpatterns=[
    path('profile',views.profile, name="profile"),
    path('createquiz',views.createquiz, name="createquiz"),
    path('updatequiz/<str:pk1>/', views.updatequiz, name="updatequiz"),
    path('reviewquiz',views.reviewquiz, name="reviewquiz"),
    path('deletequiz/<str:pk>/',views.deletequiz, name="deletequiz"),
    path('index',views.index, name="index"),
    path('kemail',views.kemail, name="kemail"),
    path('exam',views.exam, name="exam"),
    path('k7solution',views.k7solution, name="k7solution"),
    path('kbye',views.kbye, name="kbye"),
    
    path('createexam',views.createexam, name="createexam"),
    path('reviewexam',views.reviewexam, name="reviewexam"),
    path('updateexam/<str:pk1>/', views.updateexam, name="updateexam"),
    path('deleteexam/<str:pk>/',views.deleteexam, name="deleteexam"),
]