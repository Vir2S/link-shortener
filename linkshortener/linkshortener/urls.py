from django.contrib import admin
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from app.views import UrlListViewSet, UrlShortener, UrlExport, ShortUrlView


router = DefaultRouter()
router.register('api', UrlListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/shortener/(?P<origin_uri>.+)$', UrlShortener.as_view()),
    path('api/export/', UrlExport.as_view()),
    re_path(r'^api/(?P<hash>.+)$', ShortUrlView.as_view()),
]

urlpatterns += router.urls
