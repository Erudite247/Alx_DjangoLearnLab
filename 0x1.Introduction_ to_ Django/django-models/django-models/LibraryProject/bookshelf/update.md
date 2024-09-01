from bookshelf.models import Book

# Retrieving the book  title 
book = Book.objects.get(title = "1984")


# Update the book title
book.title = "Nineteen Eighty-Four"
book.save()

# checking to see if  the title was updated
updated_book = Book.objects.get(title = "Nineteen Eighty-Four")
print(updated_book.title)

output: 

Nineteen Eighty-Four




