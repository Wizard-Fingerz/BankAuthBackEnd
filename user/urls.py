from django.urls import path, include
from .views import *
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', Register.as_view(), ),
    path('user', UserView.as_view(), name='user'),
    path('security', SecurityQuestion().as_view(), name='security'),
    # path('create_user/', create_user),
]