from django import forms
from django.forms.widgets import Select
from django.utils.encoding import force_text
from django.utils.html import escape, conditional_escape

# iterable 
COURSE_CHOICES =( 
     ('-- Grado escolar --', 
       [
            
            ("1", "kinder"),
            ("2", "Primer año de Primaria"),  
            ("3", "Segundo año de Primaria"), 
            ("4", "Tercer año de Primaria"), 
            ("5", "Cuarto año de Primaria"), 
            ("6", "Quinto año de Primaria"), 
            ("7", "Sexto año de Primaria"), 
            ("8", "Primer año de Secundaria"), 
            ("9", "Segundo año de Secundaria"), 
            ("10", "Tercer año de Secundaria"),
       ]
     ),
) 

PLAN_CHOICES =( 
    ('-- Plan de ínteres --', 
      (
        ("1", "Básico"),
        ("2", "Avanzado"),
        ("3", "Premium"), 
        ("4", "CONDUSEF"), 
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
    grade = forms.ChoiceField(label='',choices = COURSE_CHOICES)
    plan = forms.ChoiceField(label='',choices = PLAN_CHOICES)
    
    

