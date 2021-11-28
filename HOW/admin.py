from django.contrib import admin
from HOW.models import Assist
from HOW.forms import AssistForm


class AssistAdmin(admin.ModelAdmin):
    form = AssistForm
    fieldsets = ('name', 'cpf', 'telephone', 'email', 'address'))
    admin.site.register(Assist, AssistAdmin)
