"""ludmag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from core import  views as core_views
from django.conf.urls import include

urlpatterns = [
    path('',core_views.home,name="home"),
    path('info/',core_views.doubt,name="doubt"),
    path('teacher/2021040<int:profesor_id>/',core_views.resume,name="resume"),
    path('fq/',core_views.team,name="nuestro_equipo"),
    path('uc/',core_views.stop,name="stop"),
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
]
if settings.DEBUG :
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
