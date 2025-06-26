from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logOut/', views.logOut, name='logOut'),
    path('cargarXML/', views.cargarXML, name='cargarXML'),
    path('verXML/', views.verXML, name='verXML'),
    path('subirXML/', views.subirXML, name='subirXML'),
    path('verConfigs/', views.verConfigs, name='verConfigs'),
    path('user_page/', views.user_page, name='user_page'),
    path('misAnimales/', views.misAnimales, name='misAnimales'),
    path('reporteAnimales/', views.reporteAnimales, name='reporteAnimales')
]