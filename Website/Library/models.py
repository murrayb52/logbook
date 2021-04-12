from django.db import models
import json


class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    import_date = models.DateTimeField('date added', null=True)
    is_in_stock = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)

