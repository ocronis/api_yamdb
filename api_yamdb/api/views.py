from reviews.models import Category, Genre, Title
from .mixins import ModelMixinSet
from .serializers import (CategorySerializer, GenreSerializer,
                         TitleReadSerializer, TitleWriteSerializer)
from .filters import TitleFilter
from .permissions import IsAdminUserOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(ModelMixinSet):
    """Получить список всех категорий. Права доступа: Доступно без токена."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (TitleFilter, )
    search_fields = ('name', )
    field = 'slug'


class GenreViewSet(ModelMixinSet):
    """Получить список всех жанров. Права доступа: Доступно без токена."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (TitleFilter,)
    search_fields = ('name', )
    field = 'slug'


class TitleViewSet(ModelViewSet):
    """Получить список всех объектов. Права доступа: Доступно без токена."""
    queryset = Title.objects.all()
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer
