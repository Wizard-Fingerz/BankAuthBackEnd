from django.shortcuts import render
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, filters
from cryptography.fernet import Fernet
from rest_framework import views
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from .models import *
from django.db.transaction import atomic, non_atomic_requests
from cryptography.fernet import Fernet

from .models import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['post'])
    def transfer(self, request):
        sender = request.user
        recipient_id = request.data.get('recipient_id')
        amount = request.data.get('amount')
        recipient = User.objects.get(pk=recipient_id)

        # Perform transfer logic here, deducting amount from sender and adding to recipient
        transaction = Transaction.objects.create(sender=sender, recipient=recipient, amount=amount)
        transaction.save()

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def deposit(self, request):
        user = request.user
        amount = request.data.get('amount')

        # Perform deposit logic here, adding amount to user's account
        transaction = Transaction.objects.create(sender=None, recipient=user, amount=amount)
        transaction.save()

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

class TransactionListAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

