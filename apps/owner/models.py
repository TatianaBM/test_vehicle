from django.db import models
from django.utils import timezone


class Owner(models.Model):
    document = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    cellphone = models.CharField(max_length=12)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    address = models.TextField()
    photo = models.ImageField(upload_to='photos/%d', default='/photos/photo_default.jpg', blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Owner, self).save(*args, **kwargs)
