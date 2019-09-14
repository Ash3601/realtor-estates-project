from django.urls import path

# Import views to link to the urls
from . import views

urlpatterns = [
    path('login', views.login, name='login'),

    path('register', views.register, name='register'),

    path('logout', views.logout, name='logout'),


    path('dashboard', views.dashboard, name='dashboard'),

]
