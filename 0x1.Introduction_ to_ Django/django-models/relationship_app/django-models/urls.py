# relationship_app/urls.py

from django.urls import path
from .views import add_book, edit_book, delete_book, LibraryDetailView

urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]