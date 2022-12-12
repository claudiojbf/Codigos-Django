from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Nivel(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length = 3,
    )