# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/', views.EditBookView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book'),
]
