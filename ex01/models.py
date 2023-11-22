from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class List(models.Model):
    name : CharField(max_length=40)