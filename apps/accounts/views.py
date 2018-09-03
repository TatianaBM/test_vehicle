from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


@user_passes_test(lambda user: not user.username, login_url='/', redirect_field_name=None)
def auth_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home:index')
        else:
            messages.error(request, "Access denied.")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {'form': form})


def auth_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
