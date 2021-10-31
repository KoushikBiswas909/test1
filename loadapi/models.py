from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    new = models.BooleanField(default=False)
    old = models.BooleanField(default=False)
    both = models.BooleanField(default=False)
    nothing = models.BooleanField(default=False)
    minimum_q = models.CharField(max_length=1)
    maximum_q = models.CharField(max_length=1)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name
