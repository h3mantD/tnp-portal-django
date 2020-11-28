from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings
import os
import re
from . import views

""" app_name = 'tnpPortal' """

urlpatterns = [
    path('', views.home, name='index'),
    path('signUp', views.signUp, name='signUp'),
    #path('aboutus/', views.aboutUs, name='aboutUs'),

    path('student', views.studLogin, name='studLogin'),
    path('student/<int:id>', views.studDetails, name='studDetails'),
    path('notification/<int:id>', views.notify, name='notification'),

    path('admin', views.adminLogin, name='adminLogin'),
    path('shortList', views.shortList, name='shortlist'),
    path('getStudData', views.getStudData, name='getStudData'),


    path('logout', views.logout, name='logout'),
    path('student/logout', views.logout, name='logout'),
    path('notification/logout', views.logout, name='logout'),

    
]
