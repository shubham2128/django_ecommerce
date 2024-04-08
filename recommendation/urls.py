from recommendation import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', views.recommendations_view , name='RecommendationPage'),
]