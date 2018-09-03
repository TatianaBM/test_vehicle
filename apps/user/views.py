from django.shortcuts import render, redirect
from apps.user.form import RegisterForm, User
from django.contrib import messages


def user_list(request):
    return render(request, "list_user.html", {'users': User.objects.all()})


def user_add(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Good, action correct.")
            return redirect('user:list')
        else:
            messages.error(request, "Unregistered user.")
            return render(request, 'form_user.html', {'form': form})
    else:
        form = RegisterForm
    return render(request, 'form_user.html', {'form': form})
