from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from .models import Tour, Rating
from .serializers import TourSerializer, RatingSerializer


class TourPagePagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 100

class TourViewSet(ReadOnlyModelViewSet):
    queryset = Tour.objects.all().order_by('-created_at') # Вывод данных в обратном порядке
    serializer_class = TourSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = TourPagePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'is_active', 'min_age', 'author', 'price', 'available_spots', 'date']


class TourCreateViewSet(viewsets.ModelViewSet):  # вместо двух отдельных
    queryset = Tour.objects.all().order_by('-created_at')
    serializer_class = TourSerializer
    permission_classes = [permissions.AllowAny]
#IsAuthenticatedOrReadOnly


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


"""Келечекте бул файл өзгөрүш мүмкүн"""



