from django.db import models
#from .models import 

# Create your models here.
class Credential(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    dateTime = models.DateTimeField('DateTime')
    def __str__(self):
        return "{0} - {1}".format(self.username, self.dateTime)

class UserDetail(models.Model):
    name = models.CharField('Name', max_length=30)
    image = models.CharField('ImageURL', max_length=1024)
    college = models.CharField('College Name', max_length=40)
    roll = models.CharField('Roll',max_length=5)
    dateTime = models.DateTimeField('DateTime')
    def __str__(self):
        return "{0} - {1}".format(self.name, self.roll)
