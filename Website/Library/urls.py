from django.urls import path

from . import views

app_name = 'Library'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('library/', views.BookListView.as_view(), name='book_list'),
    path('library/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('library/import/', views.ImportView.as_view(), name='import'),
    path('library/import_book/', views.import_book, name='importer')
]