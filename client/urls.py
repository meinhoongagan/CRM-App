from django.urls import path
from .views import client_list, client_details, add_clients,clients_delete,clients_edit

urlpatterns = [
    path("client-list/", client_list, name='client_list'),
    path("client/<int:pk>/", client_details, name="client_details"),
    path("add-client/", add_clients, name="add_client"),
    path("<int:pk>/delete",clients_delete,name="clients_delete"),
    path("<int:pk>/edit",clients_edit,name="clients_edit")
]
