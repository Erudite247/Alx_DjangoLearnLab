import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # Adjust if necessary
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
from django.core.exceptions import ObjectDoesNotExist

# Query all books by a specific author (assuming you have an author object)
author_name = "Specific Author Name"
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# List all books in a library (assuming you have a library object)
library_name = "Specific Library Name"

try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(book.title)
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'.")

# Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"Librarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for the library named '{library_name}'.")