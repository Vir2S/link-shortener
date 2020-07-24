from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Url
from .serializers import UrlSerializer


class UrlListViewSets(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()


class UrlShorter(APIView):
    def post(self, request, origin_uri):
        try:
            url = Url.objects.get(url=origin_uri)
        except:
            url = Url(url=origin_uri)
            url.save()

        short_url = url.short_url

        return Response(short_url)