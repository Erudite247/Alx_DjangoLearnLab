from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    response_text = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(response_text, content_type="text/plain")



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
