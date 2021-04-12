from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse, request
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import redirect
from . import services
import requests
from .models import Book
import json
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'Library/home.html'


# Add books to library using ISBN number
def import_book(request):
    isbn = request.POST['isbn_box']
    # add imported book to database unless already there
    book, created = Book.objects.get_or_create(isbn=isbn)
    book_data = services.get_book(isbn)
    book.title = book_data["title"]
    book.author = services.get_author_name(book_data["authors"][0]["key"])
    book.import_date = timezone.now()
    book.quantity += 1
    book.save()
    # redirect_url = 'Library/book_detail/' + str(book.pk)
    return HttpResponseRedirect(reverse('Library:book_detail', args=(book.pk,)))


class ImportView(generic.TemplateView):
    template_name = 'Library/import.html'

    """
    def get_book_details(self):
        url = "https://openlibrary.org/isbn/9780446310789.json"
        # params = {'publishers': publishers}
        response = requests.get(url).json()
        # book_dict = {'response': response}
        return render(request, 'Library/import.html', {'response': response})
    """


# Display a list of my books
class BookListView(generic.ListView):
    # ListView generic view uses a default template called
    # <app name>/<model name>_list.html; we use template_name to tell ListView
    # to use our existing "Library/books_list.html" template.
    template_name = 'Library/book_list.html'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        # Return the 10 most recently added books.
        # Book.objects.filter(import_date__lte=timezone.now()) returns a queryset
        # containing Books whose add_date is earlier than or equal to timezone.now().
        return Book.objects.filter(import_date__lte=timezone.now()).order_by('-import_date')[:10]



class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'Library/book_detail.html'


    #def get_book_details(year, author):

