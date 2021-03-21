from django import forms
from django.forms.widgets import Select
from django.utils.encoding import force_text
from django.utils.html import escape, conditional_escape
from .models import ClientePotencial,Plan,Grado,Curso



# iterable 
PLAN_CHOICES =( 
     ('-- Curso de ínteres --', 
       [
            (1, "kinder"),
            (2, "Primaria"),  
            (3, "Secundaria"),
            (4, "CONDUSEF"),
       ]
     ),
) 

GRADE_CHOICES =( 
    ('-- Grado escolar --', 
      (
        ("1", "Básico"),
        ("2", "Avanzado"),
        ("3", "Premium"), 
      )
    ),
)




class SelectWithDisabled(Select):
    """
    Subclass of Django's select widget that allows disabling options.
    To disable an option, pass a dict instead of a string for its label,
    of the form: {'label': 'option label', 'disabled': True}
    """
    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_text(option_value)
        if (option_value in selected_choices):
            selected_html = u' selected="selected"'
        else:
            selected_html = ''
        disabled_html = ''
        if isinstance(option_label, dict):
            if dict.get(option_label, 'disabled'):
                disabled_html = u' disabled="disabled"'
            option_label = option_label['label']
        return u'<option value="%s"%s%s>%s</option>' % (
            escape(option_value), selected_html, disabled_html,
            conditional_escape(force_text(option_label)))

class Formulario (forms.Form) :
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Nombre'}), error_messages={'required': 'Completa este campo'},max_length=100)
    lastname = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Apellido'}),error_messages={'required': 'Completa este campo'}, max_length=100)
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Correo'}),error_messages={'required': 'Completa este campo'})
    phone = forms.IntegerField(label='',widget=forms.TextInput(attrs={'placeholder': 'Télefono'}),error_messages={'required': 'Completa este campo'})
    plan = forms.ChoiceField(label='',choices = PLAN_CHOICES)
    grade = forms.ChoiceField(label='',choices = GRADE_CHOICES)



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



    
  