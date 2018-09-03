from django.urls import path
from apps.accounts import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.auth_login, name="login"),
    path('logout', views.auth_logout, name="logout"),

]
