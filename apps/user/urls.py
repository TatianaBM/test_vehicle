from django.urls import path
from apps.user.views import *
from django.contrib.auth.decorators import login_required

app_name = "user"

urlpatterns = [
    path('', login_required(user_list), name="list"),
    path('add', login_required(user_add), name="add"),
]
