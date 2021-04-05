from django.db import models


# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    import_date = models.DateTimeField('date added')
    ISBN = models.IntegerField()

    def __str__(self):
        return self.book_title

    """
    def is_in_stock(self):
            
    """