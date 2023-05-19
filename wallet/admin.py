from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ( 'user' ,'amount')
    
@admin.register(Wallet)
class WalletAdmin(ImportExportModelAdmin):
    list_display = ('user', 'balance', 'account_number', 'bank', 'phone_number', 'created_at')

@admin.register(WalletTransaction)
class WalletTransactionAdmin(ImportExportModelAdmin):
    list_display = ('transaction_id', 'status', 'transaction_type', 'amount', 'date')