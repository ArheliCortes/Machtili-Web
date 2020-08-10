from django.shortcuts import render
from django.shortcuts import HttpResponse
from .form import Formulario
# Create your views here.

def home (request):
    if request.method == "POST" :
        print("------------Entre a Post------------")
        response = sendEmail(request)
    else:
        context = {} 
        context['form'] = Formulario() 
        template_name = "core/home.html"
        response = render(request,template_name,context)    
    return response 

def sendEmail(request):
    username = request.POST['username']
    lastname = request.POST['lastname']
    email = request.POST['email']
    phone = request.POST['phone_number']
   
    print("------------user :",username,lastname,email,phone)
    template_name = "core/home.html"
    response = render(request,template_name) 
    return response