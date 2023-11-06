from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='weather'),
    path('forecast',views.forecast,name='forecast'),
    path('subscribe',views.subscribe,name='subscribe'),
    path('mail',views.sendmail,name='mail'),

    
]