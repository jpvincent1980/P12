from django.contrib.auth.models import AbstractUser
from django.db import models


DEPARTMENTS_CHOICES = [
    ("SALES", "Sales"),
    ("SUPPORT", "Support"),
    ("MANAGEMENT", "Management"),
    ("OTHERS", "Others")
]


class CustomUser(AbstractUser):
    """
    A model that represents a user
    """
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=20,
                                  choices=DEPARTMENTS_CHOICES,
                                  default="OTHERS")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ["-id", ]
        verbose_name = "Utilisateur"
