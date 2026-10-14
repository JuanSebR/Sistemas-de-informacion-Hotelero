from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label='Nombre(s)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan'})
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label='Apellido(s)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Pérez'})
    )
    email = forms.EmailField(
        required=True,
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'})
    )

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            if 'class' not in self.fields[field_name].widget.attrs:
                self.fields[field_name].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.rol = Usuario.Rol.CLIENTE
        if commit:
            usuario.save()
        return usuario
