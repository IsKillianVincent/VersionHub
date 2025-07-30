from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views.user_viewset import UserViewSet
from users.views.user_setting_viewset import UserSettingViewSet
from users.views.user_code_viewset import UserCodeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'user-settings', UserSettingViewSet, basename='user-settings')
router.register(r'user-codes', UserCodeViewSet, basename='user-code')

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]