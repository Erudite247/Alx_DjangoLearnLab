# relationship_app/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

class AddBookView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book_list')  # Redirect after successful addition

class EditBookView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book_list')  # Redirect after successful update

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')  # Redirect after successful deletion
