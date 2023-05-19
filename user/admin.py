from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ( 'username' ,'first_name', 'account_number', 'is_admin', 'is_customer',)
    
@admin.register(SecurityQuestions)
class SeccurityQuestionsAdmin(ImportExportModelAdmin):
    list_display = ('user', 'question1', 'answer1', 'question2', 'answer2', 'question3', 'answer3', 'question4', 'answer4',)


admin.site.site_header = "BankAuth Administration Dashboard"