from django.urls import path
from apps.vehicle import views
from django.contrib.auth.decorators import login_required

app_name = "vehicle"

urlpatterns = [
    path('', login_required(views.vehicle_list), name="list"),
    path('add', login_required(views.vehicle_add), name="add"),
    path('edit/<id_vehicle>', login_required(views.vehicle_edit), name="edit"),
    path('delete/<id_vehicle>', login_required(views.vehicle_delete), name="delete")
]
