from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import IncomeListAPIViewSerializer, IncomeDetailAPIViewSerializer
from .models import Income
from .permissions import IsOwner


# Create your views here.

class IncomeListAPIView(ListCreateAPIView):
    serializer_class = IncomeListAPIViewSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Income.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeDetailAPIViewSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Income.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
