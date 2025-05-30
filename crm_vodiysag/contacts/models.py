from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"
