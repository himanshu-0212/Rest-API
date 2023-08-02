from django.db import models

# Create your models here.

class Element(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name