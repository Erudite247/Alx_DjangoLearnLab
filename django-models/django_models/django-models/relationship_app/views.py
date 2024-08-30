# relationship_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Book, Library

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Your logic for adding a book
    pass

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Your logic for editing a book
    pass

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Your logic for deleting a book
    pass

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
