from django.urls import path, include
from rest_framework.routers import DefaultRouter
from system.views.language_viewset import LanguageViewSet
from system.views.timezone_viewset import TimezoneViewSet

router = DefaultRouter()
router.register(r'languages', LanguageViewSet, basename='language')
router.register(r'timezones', TimezoneViewSet, basename='timezone')

urlpatterns = [
    path('', include(router.urls)),
]