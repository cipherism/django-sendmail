from django.urls import path
from .views import SubscribeView, success_subs, subscribe

app_name = 'Appserver'

urlpatterns = [
    path('', subscribe, name='subscribe'),
    path('success/', success_subs, name='success_subs')
]