from django.urls import path, include
from . import views


urlpatterns = [
    path('facultydashboard/<str:pk>', views.faculty, name= 'faculty'),
    path('facultydashboard/<str:fac_id>/student/<str:stu_id>/', views.studentdetail, name= 'studentdetail'),
    path('logout/', views.logout, name= 'logout'),

]
