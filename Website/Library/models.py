from django.db import models
import json


# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    import_date = models.DateTimeField('date added')
    ISBN = models.IntegerField()

    other_detail = models.TextField(default="{}")

    """
    @property
    def other_detail_json(self):
        return json.loads(self.other_detail)

    def __str__(self):
        return self.book_title

    def is_in_stock(self):
            
    """