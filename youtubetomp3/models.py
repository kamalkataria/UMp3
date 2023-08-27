from django.db import models

class Filedownloaded(models.Model):
    filepath=models.CharField(max_length=500,default="test")
