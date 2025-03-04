from django.urls import path
from .views import LendingListCreateView, LendingDetailView


app_name = 'lendings'

urlpatterns = [
    path('', LendingListCreateView.as_view(), name='lendings-list'),
    path('<int:pk>/', LendingDetailView.as_view(), name='lending-detail'),
]