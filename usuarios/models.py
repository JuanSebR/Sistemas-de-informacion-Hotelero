from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    class Rol(models.TextChoices):
        CLIENTE = 'CLIENTE', 'Cliente'
        RECEPCIONISTA = 'RECEPCIONISTA', 'Recepcionista'
        GERENTE = 'GERENTE', 'Gerente'
        ADMIN = 'ADMIN', 'Administrador'

    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.CLIENTE,
        verbose_name='Rol'
    )

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
