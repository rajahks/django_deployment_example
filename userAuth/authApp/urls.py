from django.urls import path
from authApp import views as authAppViews

app_name = 'authApp'

urlpatterns = [
    path('registration/', authAppViews.registration,name='registration'),
    path('login/', authAppViews.user_login, name='login'),
    #path('logout/',authAppViews.user_logout, name='logout')
]
