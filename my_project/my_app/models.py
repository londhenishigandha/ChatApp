from django.db import models

# Create your models here.


class Registration(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    emp_id = models.CharField(max_length=50)
    mobileno = models.IntegerField()
    password = models.CharField(max_length=10)
    date = models.DateField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname
