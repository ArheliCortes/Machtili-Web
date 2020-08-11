from django import forms

# iterable 
COURSE_CHOICES =( 
    ("1", "Primer año de Primaria"), 
    ("2", "Segundo año de Primaria"), 
    ("3", "Tercer año de Primaria"), 
    ("4", "Cuarto año de Primaria"), 
    ("5", "Quinto año de Primaria"), 
    ("6", "Sexto año de Primaria"), 
    ("7", "Primer año de Secundaria"), 
    ("8", "Segundo año de Secundaria"), 
    ("9", "Tercer año de Secundaria")
) 

PLAN_CHOICES =( 
    ("1", "Básico"),
    ("2", "Avanzado"),
    ("3", "Premium") 
)
  
class Formulario (forms.Form) :
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Nombre'}), error_messages={'required': 'Completa este campo'},max_length=100)
    lastname = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Apellido'}),error_messages={'required': 'Completa este campo'}, max_length=100)
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Correo'}),error_messages={'required': 'Completa este campo'})
    phone = forms.IntegerField(label='',widget=forms.TextInput(attrs={'placeholder': 'Télefono'}),error_messages={'required': 'Completa este campo'})
    grade =  forms.ChoiceField(label='',choices = COURSE_CHOICES) 
    plan = forms.ChoiceField(label='',choices = PLAN_CHOICES)

