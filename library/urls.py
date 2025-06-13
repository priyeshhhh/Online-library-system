from django.urls import path
from django.shortcuts import redirect
from .views import *

urlpatterns = [
    path('', lambda request: redirect('author-list')),
    path('authors/add/', AuthorCreateView.as_view(), name='author-add'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('records/add/', BorrowRecordCreateView.as_view(), name='borrowrecord-add'),
    path('records/', BorrowRecordListView.as_view(), name='borrowrecord-list'),
    path('export/', ExportToExcelView.as_view(), name='export-excel'),
]
