from django.contrib import admin
from django.urls import path,include
from . import views
app_name='donate'
urlpatterns = [
    path('',views.index,name="home"),
    path('thanks/',views.thanks,name="thanks"),
]
