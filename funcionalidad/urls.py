from django.urls import path, re_path
from funcionalidad import views
from django.views.static import serve
from django.conf import settings
from django.contrib.auth import views as auth_views 

urlpatterns = [

path ('', views.inicial, name='inicio'),
path ('registrar', views.registrar, name = 'registrar'),
path ('ingresar', views.ingresar, name = 'ingresar'),
path('registros', views.danshboard, name='registros'),
path ('micuenta', views.cuenta, name = 'micuenta'),
path ('nuevopersonal', views.personal, name='nuevopersonal'),
path('editar/<id>/', views.editar, name='editar'),
path('eliminar/<id>/', views.eliminar, name='eliminar'),

]



urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]
