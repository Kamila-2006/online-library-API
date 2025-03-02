from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(optional=True)
    birth_date = models.DateField(optional=True)
    nationality = models.CharField(max_length=100)