from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # traerá todos
    # queryset = Category.objects.all()

    # traerá solo los publicados
    queryset = Category.objects.filter(published=True)

    # para filtrar enves de id por otro parámetro
    lookup_field = 'slug'

    # filtar por parámetros
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']