from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('signup/',views.SignupPage.as_view(),name='signup'),
    
]