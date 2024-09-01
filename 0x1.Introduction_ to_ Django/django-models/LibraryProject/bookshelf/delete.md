

from bookshelf.models import Book

# Retrieving the book
book = Book.objects.get(title = "Nineteen Eighty-Four")

# Delete the book
book.delete()
print(Book.objects.all())

# checking to see that the book was deleted
print(Book.objects.filter(title="Nineteen Eighty-Four").exists())

output:
False
