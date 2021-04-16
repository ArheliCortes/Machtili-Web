from django import forms
from django.forms.widgets import Select
from django.utils.encoding import force_text
from django.utils.html import escape, conditional_escape
from .models import ClientePotencial,Plan,Grado,Curso


class FormDoubts(forms.Form) :
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Tu Nombre'}),error_messages={'required':'Completa este campo'},max_length=100)
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder':'Tu Correo'}),error_messages={'required':'Completa este campo'})
    phone = forms.IntegerField(label='',widget=forms.TextInput(attrs={'placeholder':'Número de Contacto'}),error_messages={'required':'Completa este campo'})
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Cuentanos tus dudas.'}),error_messages={'required':'Completa este campo'})

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name

class ClientePotencialForm(forms.ModelForm):

    class Meta:
        model = ClientePotencial
        fields = ['name', 'lastname','email', 'phone','curso', 'grado','plan']
                
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre(s)'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Apellidos'}),
            'email': forms.TextInput(attrs={'placeholder': 'usuario@ejemplo.com'}),
            'phone' : forms.TextInput(attrs={'placeholder':'(52) 550 000 0000'}),
        }
        labels = {
            "name": "",
            "lastname": "",
            "email": "",
            "phone": "",
            "curso": "Curso de ínteres",
            "grado": "",
            "plan": "",

        }



    
  