from promotions import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', views.promotions_view , name='PromoPage'),
]