from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.TextField()
    isbn_number = models.IntegerField()
    genre = models.CharField(max_length=32)
    prize = models.IntegerField()