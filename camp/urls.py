from django.contrib import admin
from django.urls import path,include
from . import views
app_name='camp'
urlpatterns = [
    path('',views.index,name="home"),
    path('donate/',include("donate.urls",namespace="donate")),
    # path('buy/',include("buy.urls",namespace="buy")),
    # path('camp/',include("camp.urls",namespace="camp")),
    path('register/',include("register.urls",namespace="register")),
    path('history/',include("history.urls",namespace="history")),
]
