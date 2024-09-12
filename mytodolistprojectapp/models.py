from django.db import models

# Create your models here.

class Data(models.Model):
    Title=models.CharField(max_length=50)
    Description=models.TextField() 
    Date=models.DateField()