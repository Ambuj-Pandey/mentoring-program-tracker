from django.urls import path
from . import views

urlpatterns = [
    path('AdminPage', views.Adminpage, name= 'admin'),
]
