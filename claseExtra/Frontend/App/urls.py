from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cargarXML/', views.cargarXML, name='cargarXML'),
    path('verXML/', views.verXML, name='verXML'),
    path('subirXML/', views.subirXML, name='subirXML'),
    path('verLibros/', views.verLibros, name='verLibros')
]