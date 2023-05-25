from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
# router.register(r'transaction_list', TransactionListAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('transactions_list/', TransactionListAPIView.as_view(), name='transaction-list'),
]
