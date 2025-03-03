from django.urls import path
from .views import AuthorListView, AuthorCreateView, AuthorDetailView


app_name = 'authors'

urlpatterns = [
    path('', AuthorListView.as_view(), name='authors-list'),
    path('create/', AuthorCreateView.as_view(), name='author-create'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]