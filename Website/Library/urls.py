from django.urls import path

from . import views

app_name = 'Library'
urlpatterns = [
    path('library/', views.BookListView.as_view(), name='book_list'),
    path('library/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('library/import/', views.import_book, name= 'import'),
]