from django.forms import ModelForm
from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'age', 'salary', 'email', 'date_of_birth', 'photo', 'doc_id']
