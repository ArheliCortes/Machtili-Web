from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError
from .form import Formulario
# Create your views here.

def home (request):
    if request.method == "POST" :
  
        response = sendEmail(request)
    else:
        context = {} 
        context['form'] = Formulario() 
        template_name = "core/home.html"
        response = render(request,template_name,context)    
    return response 

def sendEmail(request):
    form = Formulario(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        lastname = form.cleaned_data['lastname']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        grade = form.cleaned_data['grade']
        grade_opt = dict(form.fields['grade'].choices)[grade]      
        plan = form.cleaned_data['plan']
        plan_opt = dict(form.fields['plan'].choices)[plan]
        
        subject =  "Machtili - Un nuevo cliente solicita información"
        from_email = settings.EMAIL_HOST_USER
        to = form.cleaned_data['humad.ludimagistri@gmail.com']

        text_content = "Contactate con :"+name+" "+lastname+"tel: "+str(phone)+" Le interesa el  plan:"+plan_opt+" del grado:"+grade_opt
        html_content = "<p>Contactate con : <strong>"+name+" "+lastname+"</strong> <br> tel: <strong>"+str(phone)+"<br> correo: <strong>"+email+"</strong><br> Le interesa el  plan:<strong>"+plan_opt+"</strong><br>Grado escolar:<strong>"+grade_opt+"</strong></p>"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
       
        if subject and msg and from_email:
            try:
                msg.send()
            except BadHeaderError:
                return HttpResponse('Se encontró un encabezado no válido.')
       
        else:
            return HttpResponse('Asegúrese de que todos los campos estén ingresados ​​y sean válidos.')

        return HttpResponseRedirect('')
    else :
        form= Formulario()
    
    return render(request, 'core/home.html', {'form': form})