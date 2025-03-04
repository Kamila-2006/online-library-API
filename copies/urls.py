from django.urls import path
from .views import CopiesListCreateView, CopyDetailView


app_name = 'copies'

urlpatterns = [
    path('', CopiesListCreateView.as_view(), name='copies-list'),
    path('<int:pk>/', CopyDetailView.as_view(), name='copy-detail'),
]