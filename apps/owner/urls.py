from django.urls import path
from apps.owner import views
from django.contrib.auth.decorators import login_required

app_name = "owner"

urlpatterns = [
    path('', login_required(views.owner_list), name="list"),
    path('add', login_required(views.owner_add), name="add"),
    path('edit/<id_owner>', login_required(views.owner_edit), name="edit"),
    path('details/<id_owner>', login_required(views.owner_details), name="detail"),
    path('delete/<id_owner>', login_required(views.owner_delete), name="delete")
]
