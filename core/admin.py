from django.contrib import admin
from .models import Client, ID, Sale, Product


class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'last_name', 'age', 'salary', 'photo', 'doc_id']
    list_display = ['name', 'last_name', 'age', 'salary', ]
    list_filter = ['name', 'last_name', 'age', 'salary', ]
    search_fields = ['name', 'last_name', 'age', 'salary']


class SaleAdmin(admin.ModelAdmin):
    fields = ['sale_number', 'client', 'total', 'products']
    list_display = ['sale_number', 'client', ]
    list_filter = ['sale_number', 'client', ]
    search_fields = ['sale_number', 'client', ]


admin.site.register(Client, ClientAdmin)
admin.site.register(ID)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Product)
