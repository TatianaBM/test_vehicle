from apps.owner.models import *


class Type(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Brand(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Model(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Vehicle(models.Model):
    enrollment = models.CharField(max_length=10, unique=True)
    owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, auto_now=True)
    modified = models.DateTimeField(editable=True, auto_now=True)
    color = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos_cars/%d', default='/photos_cars/photo_car_default.png', blank=True)



