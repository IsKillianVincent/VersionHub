from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views.user_viewset import UserViewSet
from users.views.user_settings_viewset import UserSettingsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'user-settings', UserSettingsViewSet, basename='user-settings')

urlpatterns = [
    path('', include(router.urls)),
]