from django.urls import path
from .views import wechat_login

urlpatterns = [
    path('wechat_login', wechat_login),
]
