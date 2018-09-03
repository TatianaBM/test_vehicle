from django.shortcuts import render, redirect
from apps.vehicle.forms import Vehicle, VehicleForm
from apps.owner.forms import Owner
from django.contrib import messages
from django.db.models import Q


def vehicle_list(request):
    parameter = request.GET.get('parameter', None)

    messages.success(request, parameter)
    if parameter:
        ids = Owner.objects.values_list('id', flat=True).filter(
            Q(first_name__icontains=parameter) | Q(last_name__icontains=parameter) | Q(
                document__icontains=parameter)).all()

        vehicles = Vehicle.objects.filter(Q(enrollment__icontains=parameter) | Q(owner_id__in=set(ids))).all()
    else:
        vehicles = Vehicle.objects.all()

    context = {
        'vehicles': vehicles,
        'parameter': parameter,
    }

    return render(request, "list_vehicle.html", context)


def vehicle_add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Good, action correct.")
            return redirect('vehicle:list')
        else:
            messages.error(request, "Error, action incorrect.")
            return render(request, 'form_vehicle.html', {'form': form, 'is_add': True})

    else:
        form = VehicleForm()
    return render(request, 'form_vehicle.html', {'form': form, 'is_add': True})


def vehicle_edit(request, id_vehicle):
    vehicle = Vehicle.objects.get(id=id_vehicle)
    if request.method == 'GET':
        form = VehicleForm(instance=vehicle)
    else:
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, "Good, action correct.")
            return redirect('vehicle:list')
        else:
            messages.error(request, "Error, action incorrect.")
            return render(request, 'form_vehicle.html', {'form': form})

    return render(request, 'form_vehicle.html', {'form': form})


def vehicle_delete(request, id_vehicle):
    vehicle = Vehicle.objects.get(id=id_vehicle)
    if request.method == 'POST':
        vehicle.delete()
        messages.success(request, "Good, action correct.")
        return redirect('vehicle:list')
    return render(request, 'delete_vehicle.html', {'context': vehicle})
