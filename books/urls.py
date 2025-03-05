from django.urls import path
from .views import BookListCreateView, BookDetailView, BookCopiesView

app_name = 'books'

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('<int:pk>/copies/', BookCopiesView.as_view(), name='book-copies')
]