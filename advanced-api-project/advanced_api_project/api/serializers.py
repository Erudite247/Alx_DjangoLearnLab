from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Validates that the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Validate that the publication year is not in the future.
        """
        if value > 2024:  # Adjust the current year if needed
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested BookSerializer to represent related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
