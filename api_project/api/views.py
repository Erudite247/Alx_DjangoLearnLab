#views.py

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# BookList view
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet
class BookViewSet(viewsets.ModelViewSet):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookViewSet(ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]