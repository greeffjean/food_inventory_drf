from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=60)
    origin = models.CharField(max_length=60)

    def __str__(self):
        return self.name
