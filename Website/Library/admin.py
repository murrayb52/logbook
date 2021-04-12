from django.contrib import admin
from .models import Book
# Register your models here.


class LibraryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ISBN', {'fields': ['isbn']}),
        ('Title', {'fields': ['title']}),
        ('Author', {'fields': ['author']}),
        ('#', {'fields': ['quantity']}),
        ('In stock', {'fields': ['is_in_stock']}),
        ('Cover URL', {'fields': ['cover_url']}),
        ('Date information', {'fields': ['import_date'], 'classes': ['collapse']}),

    ]

    list_display = ('isbn', 'title', 'author', 'quantity', 'import_date')
    # This adds a filter sidebar option to the admin page to filter out questions by pub_date
    list_filter = ['title']
    # Search capability
    search_fields = ['book_title', 'author']

admin.site.register(Book, LibraryAdmin)