from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    # Python 3
    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()

class Hipertension(models.Model):
    usuario= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=24)
    apellido = models.CharField(max_length=24)
    presion_s = models.DecimalField(max_digits=5, decimal_places=2)
    edad= models.IntegerField(null= True)
    genero= models.CharField(max_length=24, null=True)
    imc= models.DecimalField(max_digits=5, decimal_places=2, null= True)
    presion_d=models.IntegerField(null= True)
    colesterol_t= models.DecimalField(max_digits=5, decimal_places=2, null=True)