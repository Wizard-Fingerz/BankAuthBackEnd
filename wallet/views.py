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

# Create your views here.

key = Fernet.generate_key()
# print(key)
f = Fernet(key)
# print(f)



@login_required
@verified
def dashboard(request):
    wallet = get_object_or_404(Wallet, user=request.user)
    return render(request, "dashboard.html", context={"wallet":wallet})

@login_required
def create_wallet(request):
    form = BVNForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            bvn = cd["bvn"]
            new_wallet = wallet.create_user_wallet(
                    first_name= user.first_name,
                    last_name= user.last_name,
                    email=user.email,
                    date_of_birth= user.date_of_birth.strftime('%Y-%m-%d'),
                    bvn= str(bvn)
                )
            if new_wallet["response"]["responseCode"] == '200':
                user.verified = True
                user.save()
                Wallet.objects.create(
                    user = user,
                    balance = new_wallet["data"]["availableBalance"],
                    account_name = new_wallet["data"]["accountName"],
                    account_number = new_wallet["data"]["accountNumber"],
                    bank = new_wallet["data"]["bank"],
                    phone_number = new_wallet["data"]["phoneNumber"],
                    password = fernet.encrypt(new_wallet["data"]["password"].encode())
                )
                messages.success(request, "Account verified, wallet successfully created")
                return redirect("accounts:dashboard")
            else:
                messages.error(request, new_wallet["response"]["message"])
           
    return render(request, "accounts/bvn.html", context = {"form":form})

def make_transaction(request):
    if request.method == 'POST':
        try:
            sender = request.POST.get('sender')
            recipient = request.POST.get('recipient')
            amount = request.POST.get('amount')
            
            with transaction.atomic():
                sender_obj = Payment.objects.get(user = sender)
                sender_obj.amount -= int(amount)
                sender_obj.save()
                
                recipient_obj = Payment.objects.get(user = recipient)
                recipient_obj.amount += int(amount)
                recipient_obj.save()
                messages.success(request, 'YOur amount is transfered')
        except Exception as e:
            print(e)
            messages.success(request, 'Something went wrong')
        return redirect('/')
    return render(request, 'home.html')

