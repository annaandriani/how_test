from django.forms import ModelForm
from HOW.models import Assist


class AssistForm(ModelForm):
    class Meta:
        model = Assist
        fields = ['name', 'cpf', 'telephone', 'email', 'address']
