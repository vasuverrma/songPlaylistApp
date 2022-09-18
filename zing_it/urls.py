from django.urls import path
from zing_it import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about/',views.about,name="about"),
    path('playlist/<int:id>',views.playlist,name="playlist"),
]