from django.shortcuts import render, redirect
from apps.owner.forms import OwnerForm, Owner
from apps.vehicle.forms import Vehicle
from django.contrib import messages


def owner_list(request):
    context = {
        'owners': Owner.objects.all()
    }
    return render(request, "list_owner.html", context)


def owner_add(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Good, action correct.")
            return redirect('owner:list')
        else:
            messages.error(request, "Error, action incorrect.")
            return render(request, 'form_owner.html', {'form': form, 'is_add': True})
    else:
        form = OwnerForm()
    return render(request, 'form_owner.html', {'form': form, 'is_add': True})


def owner_edit(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    if request.method == 'GET':
        form = OwnerForm(instance=owner)
    else:
        form = OwnerForm(request.POST, request.FILES, instance=owner)
        if form.is_valid():
            form.save()
            messages.success(request, "Good, action correct.")
            return redirect('owner:list')
        else:
            messages.error(request, "Error, action incorrect.")
            return render(request, 'form_owner.html', {'form': form})

    return render(request, 'form_owner.html', {'form': form})


def owner_delete(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    if request.method == 'POST':
        owner.delete()
        messages.success(request, "Good, action correct.")
        return redirect('owner:list')
    return render(request, 'delete_owner.html', {'context': owner})


def owner_details(request, id_owner):
    owner_info = Owner.objects.get(id=id_owner)
    vehicles_list = Vehicle.objects.filter(owner=owner_info).all()

    context = {
        'owner_info': owner_info,
        'vehicles_list': vehicles_list,
    }
    return render(request, 'detail_owner.html', context)


