from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register , name='register'), #Sign Up urls
    path('login', views.login , name='login'), #Login urls
    path('logout', views.logout , name='logout'), #Logout url
]