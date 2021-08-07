from django.db import models

# Create your models here.
class Coffee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True)
