from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Car
from .serializers import CarSerializer
from .service import CarFilter
from django_filters.rest_framework import DjangoFilterBackend


class CarListViewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CarListView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)
    pagination_class = CarListViewPagination
