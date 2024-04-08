from livechat import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', views.chat , name='HomePage'),
    path('chat/', views.chat , name='LiveChat'),
]