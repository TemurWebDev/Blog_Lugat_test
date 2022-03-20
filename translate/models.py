from django.db import models

class Translate(models.Model):
    inglizcha = models.CharField(max_length=100)
    uzbekcha = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.inglizcha} - {self.uzbekcha}"
