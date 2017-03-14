from django.conf.urls import url,include
from dreamsgroup import views

urlpatterns = [
    url(r'^$',views.dreamsmain, name='dreamsmain'),
    url(r'^events-result/', views.events, name='events-result'),
    url(r'^mycollege/', views.myCollege, name='mycollege'),
    url(r'^myschool/', views.mySchool, name='myschool'),
    url(r'^writepost/', views.writepost, name='writepost'),
    url(r'^uploadpicture/', views.uploadpicture, name='uploadpicture'),
    url(r'^uploadvideo/', views.uploadvideos, name='uploadvideo')
]