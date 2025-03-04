from rest_framework import generics
from .models import Copy
from .serializers import BookCopySerializer


class CopiesListCreateView(generics.ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = BookCopySerializer

class CopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Copy.objects.all()
    serializer_class = BookCopySerializer