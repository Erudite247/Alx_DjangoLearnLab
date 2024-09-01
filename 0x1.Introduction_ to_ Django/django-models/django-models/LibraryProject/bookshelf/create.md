
from bookshelf.models import Book

# This Create a new book instance 
book = Book.objects.create(title = "1984", author="George Orwell", publication_year=1949)

# Checking to see if the book was created
print(Book.objects.all())

Ouput: 

<QuerySet [<Book: 1984 by George Orwell>]>

