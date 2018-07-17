from django.urls import path
from .views import list_clients, new_client, update_client, delete_client

urlpatterns = [
    path('', list_clients, name='client_list'),
    path('new/', new_client, name='client_create'),
    path('update/<int:id>/', update_client, name='client_update'),
    path('delete/<int:id>/', delete_client, name='client_delete'),
]
