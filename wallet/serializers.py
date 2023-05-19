from rest_framework import serializers
from .models import *


class WalletSerializer(serializer.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance', 'account_name', 'account_number', 'bank', 'pasword']
        
class PaymentSerializer(serializer.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount',]

class WalletTransactionSerializer(serializer.ModelSerializer):
    class Meta:
        model = WalletTransaction
        fields = ['status', 'transaction_type', 'wallet', 'amount', 'date']