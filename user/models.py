from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser




# Create your models here.
class User(AbstractUser):
    username = models.CharField(_('Username'), max_length = 250, null=True, blank=True, unique=True)
    first_name = models.CharField(_('First name'), max_length = 250, null=True, blank=True)
    last_name = models.CharField(_('Last name'), max_length=250)
    account_number = models.IntegerField(unique=True, null=True, blank=True)
    card_details = models.IntegerField(unique=True, null=True, blank=True)
    last_six_digits = models.IntegerField(unique=True, null=True, blank=True)
    # email = models.EmailField(_("email"), max_length=250, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_customer = models.BooleanField(default=False, verbose_name = 'Customer')
    is_bank_manager = models.BooleanField(default=False, verbose_name = 'Bank Manager')
    verified = models.BooleanField(_("verified"), default=False)
    
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'
    

    def __str__(self):
        return self.username


class SecurityQuestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question1 = models.CharField(max_length = 250)
    answer1 = models.CharField(max_length =250)
    question2 = models.CharField(max_length =250)
    answer2 = models.CharField(max_length =250)
    question3 = models.CharField(max_length =250)
    answer3 = models.CharField(max_length =250)
    question4 = models.CharField(max_length =250)
    answer4 = models.CharField(max_length =250)
    
    def __str__(self):
        return self.user