from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # main page 
    path('members', views.members, name='members'),  # now responds to /members/
    path('details/<int:id>/', views.details, name='details'),  
    path('testing', views.testing, name='testing'),  # testing page
]
