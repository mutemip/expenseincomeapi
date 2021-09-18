from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseListAPIViewSerializer, ExpenseDetailAPIViewSerializer
from .models import Expense
from .permissions import IsOwner


# Create your views here.

class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpenseListAPIViewSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Expense.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseDetailAPIViewSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Expense.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
