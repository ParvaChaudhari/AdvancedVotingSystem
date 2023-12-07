from django.contrib import admin
from django.urls import path
from voting import views

urlpatterns = [
    path("", views.index, name='voting'),
    path("about", views.about, name='about'),
    path("index", views.index, name='index'),
    path("party", views.party, name='party'),
    path("verify", views.verify, name='verify'),
    path("info", views.info, name='info'),
    path("details", views.details, name='details'),
    path("finish", views.finish, name='finish')
]