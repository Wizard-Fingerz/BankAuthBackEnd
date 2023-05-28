from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class UsernameOrAccountNumberBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if the user exists with the given username or account number
        try:
            user = User.objects.get(Q(username=username) | Q(account_number=username))
        except User.DoesNotExist:
            return None

        # Perform the password check
        if user.check_password(password):
            return user

        return None
