from django.shortcuts import render
from django. shortcuts import redirect
from django.views.generic import DetailView
from .models import Library
from. models import Book
from . models import Library

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, './list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = './templates/list_books.html'
    context_object_name = 'library'