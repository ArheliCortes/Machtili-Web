from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings

from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError
from .form import *
# Create your views here.

def home (request):
    if request.method == "POST" :
        response = sendEmailInfo(request)
    else:
        context = {} 
        context['form'] = ClientePotencialForm() 
        context['form_doubt'] = FormDoubts()
        template_name = "core/home.html"
        response = render(request,template_name,context)    
    return response 

def doubt (request):
    if request.method == "POST" :
        response = sendEmailDoubt(request)
    else:
        context = {} 
        context['form'] = ClientePotencialForm() 
        context['form_doubt'] = FormDoubts() 
        template_name = "core/home.html"
        response = render(request,template_name,context) 
    return response 

def sendEmailInfo(request):
    form = ClientePotencialForm(request.POST)
    form_info = ClientePotencialForm() 
    form_name_info='form'
    form_doubt = FormDoubts()
    form_name_doubt='form_doubt'
    context = {form_name_info: form_info,form_name_doubt:form_doubt}

    if form.is_valid():
        name = form.cleaned_data['name']
        lastname = form.cleaned_data['lastname']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        grado = str(form.cleaned_data['grado'])
        curso = str(form.cleaned_data['curso'])
        plan = str(form.cleaned_data['plan'])

        subject =  "Un nuevo cliente solicita información"
        from_email = "Machtili<"+settings.EMAIL_HOST_USER+">"
        #to = 'humad.ludimagistri@gmail.com'
        to = "arhelicortes2303@gmail.com"
        text_content = "Contactate con :"+name+" "+lastname+"tel: "+str(phone)+" Le interesa el  curso:"+curso+" del grado:"+grado+"Plan:"+plan
        html_content = "<p>Contactate con : <strong>"+name+" "+lastname+"</strong> <br> tel: <strong>"+str(phone)+"</strong><br> correo: <strong>"+email+"</strong><br> Le interesa el  curso:<strong>"+curso+"</strong><br>Grado escolar/Días:<strong>"+grado+"</strong><br>Plan:<strong>"+plan+"</strong></p>"

        msg_response = "Su información fue enviada!. Un asesor académico se comunicará con usted en breve."
        response = _sendEmail(request,subject,text_content,html_content,from_email,to,msg_response,form_name_info,form_info,form_name_doubt,form_doubt)
    else :
        response = render(request, 'core/home.html', context)
    return response


def sendEmailDoubt(request):
    form = FormDoubts(request.POST)
    form_info = ClientePotencialForm() 
    form_name_info='form'
    form_doubt = FormDoubts()
    form_name_doubt='form_doubt'

    if form.is_valid():
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        context = {form_name_info: form_info,form_name_doubt:form_doubt}

        subject = "Un cliente tiene una duda"
        msg = form.cleaned_data['message']
        from_email = "Machtili<"+settings.EMAIL_HOST_USER+">"
        #to = 'humad.ludimagistri@gmail.com'
        to = "arhelicortes2303@gmail.com"
        text_content = msg+"Contactate con :"+name+"email: "+email+"tel: "+str(phone)
        html_content = "<p>Contactate con : <strong>"+name+"</strong><br>email:<strong>"+email+"</strong><br>tel:<strong>"+str(phone)+"</strong><br><br>"+msg+"</p>"
        msg_response = "Su mensaje fue enviado. Un asesor académico tratara de aclarar todas sus dudas lo antes posible."
        response = _sendEmail(request,subject,text_content,html_content,from_email,to,msg_response,form_name_info,form_info,form_name_doubt,form_doubt)
    else :
        response = render(request, 'core/home.html', context)
    return response

def _sendEmail(request,subject,text_content,html_content,from_email,to,msg_response,form_name_info,form_info,form_name_doubt,form_doubt):

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    context={form_name_info: form_info,form_name_doubt:form_doubt}

    if subject and msg and from_email:
        try:
            msg.send()
            messages.error(request,msg_response)
        except BadHeaderError:
            return HttpResponse('Se encontró un encabezado no válido.')
    else:
        messages.warning(request, 'Asegúrese de que todos los campos estén ingresados ​​y sean válidos.')
        return render(request, 'core/home.html',context)
    
    return render(request, 'core/home.html',context)


def stop (request):
    return render(request,"core/under_construction.html")   