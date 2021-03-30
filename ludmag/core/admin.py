from django.contrib import admin
from .models import *

# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display = ("name","curso")

class CursoAdmin(admin.ModelAdmin):
    list_display = ("name",)

class GradoAdmin(admin.ModelAdmin):
    list_display = ("name","curso")

class ClientePotencialAdmin(admin.ModelAdmin):
    list_display = ("name","lastname","email","phone","curso","grado","plan")

class ParagraphInline(admin.StackedInline):
    model = Paragraph

class ProfesorAdmin(admin.ModelAdmin):
     inlines = [ParagraphInline,]
     def save_model(self, request, obj, form, change):
        obj.save()
admin.site.register(Plan,PlanAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(ClientePotencial, ClientePotencialAdmin)
admin.site.register(ProfesorResume,ProfesorAdmin)