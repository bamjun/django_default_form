from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page),
    path('<int:pk>/', views.index, name='index'),
]
