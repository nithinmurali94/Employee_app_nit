from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Employee(models.Model):
    employee_code = CharField(max_length=250)
    employee_name = CharField(max_length=250)
    department = CharField(max_length=250)
    age = IntegerField()
    experience = IntegerField()

    
