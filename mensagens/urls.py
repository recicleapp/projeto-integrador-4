from django.urls import path

from . import views

app_name = 'mensagens'

urlpatterns = [
    path('', views.mensagens, name='lista'),
]
