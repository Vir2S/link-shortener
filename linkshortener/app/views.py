from rest_framework import viewsets, mixins
from .models import Url
from .serializers import UrlSerializer


class UrlListViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
