from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone

from .models import Book
# Create your views here.


def index(request):
    return HttpResponse("Welcome to Logbook!")


# Display a list of my books
class BookListView(generic.ListView):
    # ListView generic view uses a default template called
    # <app name>/<model name>_list.html; we use template_name to tell ListView
    # to use our existing "Library/index.html" template.
    template_name = 'Library/book_list.html'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        """Return the 10 most recently added books."""
        # Book.objects.filter(import_date__lte=timezone.now()) returns a queryset
        # containing Books whose add_date is earlier than or equal to timezone.now().
        return Book.objects.filter(import_date__lte=timezone.now()).order_by('-import_date')[:10]


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'Library/book_detail.html'
