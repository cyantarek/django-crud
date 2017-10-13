from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=45)
    breed = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)