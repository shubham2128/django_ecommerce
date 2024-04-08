from . import views
from django.contrib import admin
from django.urls import path , include

app_name = 'feedback'
urlpatterns = [
    path('', views.submit_feedback , name='Feedback'),
]