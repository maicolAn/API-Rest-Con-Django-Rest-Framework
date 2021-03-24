from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView

from .models import Perfil, Hipertension
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
import joblib
import numpy as np

from rest_framework.generics import (CreateAPIView)
from perfiles.models import Hipertension


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'perfiles/bienvenida.html'


from django.contrib.auth.views import LoginView

class SignInView(LoginView):
    form_class=LoginForm
    template_name = 'perfiles/iniciar_sesion.html'

from django.contrib.auth.views import LogoutView 

class SignOutView(LogoutView):
    pass

def modelo(request):
    return render(request, "perfiles/modelo.html")

def historial(request):
    usuariop=User.objects.get(username=request.user)
    consulta=Hipertension.objects.filter(usuario=usuariop).order_by("-id")

    return render(request, "perfiles/historial.html", {"consultas":consulta})

def buscar(request):

    
    if (request.POST ["edad"] and request.POST ["presions"] and request.POST ["imc"] and request.POST [ "presiond"] and request.POST ["colesterolt"]):
        
        usuariop=User.objects.get(username=request.user)
        
        nombrep=request.POST ['nombre']
        apellidop=request.POST ['apellido']

        presionsp=request.POST ['presions']
        generop=request.POST ['select']
        edadp=request.POST ['edad']
        imcp=request.POST ['imc']
        presiondp=request.POST ['presiond']
        colesterolp=request.POST ['colesterolt']
        #usuario=User.objects.username()
        datos=Hipertension(usuario=usuariop, nombre=nombrep, apellido=apellidop,presion_s=presionsp, edad=edadp, genero=generop, imc=imcp, presion_d=presiondp, colesterol_t=colesterolp)
        datos.save()
        if(generop=="1"):
            sexo="Masculino"
        elif(generop=="2"):
            sexo="Femenino"

        modelo= joblib.load("perfiles/modelo/perfiles/modelo_entrenado.pkl")
        pca= joblib.load("perfiles/modelo/perfiles/modelo_pca.pkl")
        presionsp=int(presionsp)
        generop=int(generop)
        edadp=int(edadp)
        imcp=int(imcp)
        presiondp=int(presiondp)
        colesterolp=int(colesterolp)
        #X=np.array([[-90.4469,	-14.529,	1.09817,	-1.40543,	-4.05994]])
        X=np.array([[generop, edadp, presionsp , presiondp , colesterolp ,imcp]])
        X_pca=pca.transform(X)
        y = modelo.predict(X_pca)
        if (y == 0):
            Resultado="No hipertenso"
        elif(y==1):
            Resultado="Hipertenso"

        consulta=Hipertension.objects.filter(usuario=usuariop).order_by("-id")
        #mensaje= "Tus datos : %r" %request.POST ["nombre"]
        #mensaje=usuario
        

    else:

        Resultado="Error, llena todas las lineas"
        datos=0;
        sexo=0;
        usuariop=User.objects.get(username=request.user)
        consulta=Hipertension.objects.filter(usuario=usuariop).order_by("-id")


    return render(request, "perfiles/resultado.html", {"resultados":Resultado, "datos":datos, "sexo":sexo, "consultas":consulta})