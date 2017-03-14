from django.conf.urls import url,include
from account.views import connect,register,login,logout,dreamsjob



urlpatterns = [
    url(r'^connect/', connect, name='connect'),
    url(r'^register/', register, name='register'),
    url(r'^login/', login, name='login'),
    url(r'^loggedout/',logout, name='logout'),
    url(r'^dreamsgroup/', dreamsjob, name='dreamsjob'),
]