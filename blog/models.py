from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title