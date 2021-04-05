from django.contrib import admin
from .models import Book
# Register your models here.

class LibraryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['book_title']}),
        ('Author', {'fields': ['author']}),
        ('ISBN', {'fields': ['ISBN']}),
        ('Date information', {'fields': ['import_date'], 'classes': ['collapse']}),

    ]

    list_display = ('book_title', 'author', 'import_date', 'ISBN')
    # This adds a filter sidebar option to the admin page to filter out questions by pub_date
    list_filter = ['import_date']
    # Search capability
    search_fields = ['book_title', 'author']

admin.site.register(Book, LibraryAdmin)