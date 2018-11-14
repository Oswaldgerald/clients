from django.forms import ModelForm
from .models import Client, Product, Sale


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'age', 'salary', 'email', 'date_of_birth', 'photo', 'doc_id']


# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ['description ', 'price', 'taxes']


# class SalesForm(ModelForm):
#     class Meta:
#         model = Sale
#         fields = ['sale_number', 'client', 'total', 'date', 'products']
