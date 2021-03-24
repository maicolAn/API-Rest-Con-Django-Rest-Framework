"""PruebaUsuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import  url
from django.contrib import admin
from django.urls import path
from perfiles.views import SignUpView, BienvenidaView, SignInView, SignOutView, modelo, buscar, historial
from perfiles.api import UserAPI, PersonaList, Login, Logout
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    path('modelo/',modelo, name="Modelo"),
    path('buscar/',buscar, name="Buscar"),
    path('historial/',historial, name="Historial"),
    
    path('api/create_user/', UserAPI.as_view(), name = "api_create_user"),
    path('api/persona/', PersonaList.as_view(), name = "persona_list"),
    path('api_generate_token/', views.obtain_auth_token),
    path('login/', Login.as_view(), name = "login"),
    path('logout/', Logout.as_view(), name = "logout"),

]

