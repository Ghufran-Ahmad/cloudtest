from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Types(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    bedSize = models.CharField(max_length=60)
    wifi = models.BooleanField()
    roomService = models.BooleanField()
    breakfast = models.BooleanField()
    pool = models.BooleanField()

    def __str__(self):
        return str(self.id)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.PositiveIntegerField()
    available = models.BooleanField()
    typeid = models.ForeignKey(Types, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = CloudinaryField('display picture', blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):

        instance.Customer.save()

    def __str__(self):
        return str(self.id)


