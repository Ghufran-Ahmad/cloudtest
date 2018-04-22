from django.db import models

# Create your models here.


class Types(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    bedSize = models.CharField()
    wifi = models.BooleanField()
    roomService = models.BooleanField()
    breakfast = models.BooleanField()
    pool = models.BooleanField()

    def __str__(self):
        return self.id


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.PositiveIntegerField()
    available = models.BooleanField()
    typeid = models.ForeignKey(Types, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    fName = models.CharField()
    lName = models.CharField()
    username = models.CharField()
    Password = models.CharField()
    dp = models.ImageField()

    def __str__(self):
        return self.id


