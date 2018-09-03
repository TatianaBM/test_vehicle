from django.shortcuts import render
from apps.owner.models import Owner
from apps.vehicle.models import Vehicle
from apps.user.form import User


def home_view(request):
    total_owners = Owner.objects.all().count()
    total_users = User.objects.all().count()
    total_vehicles = Vehicle.objects.all().count()

    context = {
        'total_owners': total_owners,
        'total_vehicles': total_vehicles,
        'total_users': total_users,
    }

    return render(request, 'index.html', context)
