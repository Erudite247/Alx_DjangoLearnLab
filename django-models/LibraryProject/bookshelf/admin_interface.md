from django.contrib import admin
from .models import Book  # Import the Book model

class BookAdmin(admin.ModelAdmin):
    # displaying  list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add searching 
    search_fields = ('title', 'author')
    
    # Adding filters
    list_filter = ('publication_year',)

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
