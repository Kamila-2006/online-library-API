from django.urls import path
from .views import LendingListCreateView, LendingDetailView, LendingReturnView


app_name = 'lendings'

urlpatterns = [
    path('', LendingListCreateView.as_view(), name='lendings-list'),
    path('<int:pk>/', LendingDetailView.as_view(), name='lending-detail'),
    path('<int:pk>/return/', LendingReturnView.as_view(), name='lending-return'),
]