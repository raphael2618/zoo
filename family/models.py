from django.db import models

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cage(models.Model):
    name = models.CharField(max_length=100)
    family = models.OneToOneField(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
