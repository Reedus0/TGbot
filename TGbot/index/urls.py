from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView
from .models import Message
from .import views

urlpatterns = [
    path('', ListView.as_view(queryset = Message.objects.all(), template_name='index/index.html'), name = 'message'),
]