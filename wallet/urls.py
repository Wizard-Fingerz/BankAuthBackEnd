from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', Register.as_view()),
    path('create_user/', create_user),
]