from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer


class LendingListCreateView(generics.ListCreateAPIView):
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

class LendingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer