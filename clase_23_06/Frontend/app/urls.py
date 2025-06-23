from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard')
]