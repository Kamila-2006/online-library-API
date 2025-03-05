from rest_framework import generics
from .models import Lending
from .serializers import LendingSerializer, LendingOverdueSerializer
from rest_framework import status
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class LendingListCreateView(generics.ListCreateAPIView):
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

class LendingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

class LendingReturnView(APIView):
    def put(self, request, pk):
        lending = get_object_or_404(Lending, pk=pk)

        if lending.status != 'active':
            return Response(
                {'error': 'This book has already been returned.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        lending.status = 'returned'
        lending.returned_date = now()
        lending.book_copy.is_available = True
        lending.book_copy.save()
        lending.save()

        serializer = LendingSerializer(lending)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OverdueLendingsView(generics.ListAPIView):
    serializer_class = LendingOverdueSerializer

    def get_queryset(self):
        return Lending.objects.filter(status='overdue')
