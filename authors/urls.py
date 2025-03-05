from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView, AuthorBooksView

app_name = 'authors'

urlpatterns = [
    path('', AuthorListCreateView.as_view(), name='authors-list'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('<int:pk>/books/', AuthorBooksView.as_view(), name='author-books'),
]