
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import ListView

from . import views


app_name = 'annuaire'

urlpatterns = [

    path('', views.annuaire_list, name='index')
]
