from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.middleware import csrf
from django.contrib.auth import authenticate

from rest_framework import generics, filters, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import *
from .models import *
from cryptography.fernet import Fernet
from rest_framework import views
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from django.conf import settings
from .models import *

# Create your views here.

key = Fernet.generate_key()
print(key)
f = Fernet(key)
print(f)

def get_csrf_token(request):
    token = csrf.get_token(request)
    return JsonResponse({'csrfToken': token})



class CustomerProfileCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomerSerializer

class Register(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            # Registration code...
            user = serializer.save()
            token = Token.objects.create(user=user)
            # Get the plaintext data from the form input
            card_details = serializer.data.get('card_details')

            # Generate a Fernet key
            key = Fernet.generate_key()
            # Create a Fernet object with the key
            f = Fernet(key)
            # Encrypt the plaintext data
            card_details = f.encrypt(str(card_details).encode())

            password = make_password(serializer.data['password'])
            User.objects.filter(account_number=serializer.data['account_number']).update(
                card_details=card_details)
            User.objects.filter(account_number=serializer.data['account_number']).update(
                password=password)

            # Retrieve the token key
            token_key = token.key


            return Response({'success': 'Registration Successful.', 'token': token_key}, status=status.HTTP_201_CREATED)
        else:
            # Return the validation errors in the response
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        account_number = request.data.get('account_number')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(account_number=account_number, password=password)

        if user is not None:
            # Generate or retrieve the authentication token
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class UserView(APIView):
#     # permission_classes = (permissions.IsAuthenticated)
#     permission_classes = [permissions.AllowAny]
#     authentication_classes = (SessionAuthentication,)

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response({'user': serializer.data}, status = status.HTTP_200_OK)

#     def post(self, request):
#         serializer = UserRegisterSerializer(data = request.data)
#         if serializer.is_valid():
#             obj = serializer.save()
#             # Get the plaintext data from the form input
#             card_details = serializer.data.get('card_details')
#             # Generate a Fernet key
#             key = Fernet.generate_key()
#             # Create a Fernet object with the key
#             f = Fernet(key)
#             # Encrypt the plaintext data
#             card_details = f.encrypt(card_details.encode())

#             password = make_password(serializer.data['password'])
#             User.objects.filter(account_number=serializer.data['account_number']).update(
#                 card_details=card_details)
#             User.objects.filter(account_number=serializer.data['account_number']).update(
#                 password=password)
#             return Response({'success': 'Registration Successful.'}, status=200)
#         else:
#             return Response({'error': 'Error. Try again'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @csrf_exempt
# def create_user(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 400)



class SecurityQuestion(APIView):
    def post(self, request):
        serializer = SecurityQuestionsSerializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.save()
            # get the question and their answers from the frontend as plaintext
            question1 = serializer.data.get('question1')
            answer1 = serializer.data.get('answer1')
            question2 = serializer.data.get('question2')
            answer2 = serializer.data.get('answer2')
            question3 = serializer.data.get('question3')
            answer3 = serializer.data.get('answer3')
            question4 = serializer.data.get('question4')
            answer4 = serializer.data.get('answer4')

            # encrypt the inputs using the generated key
            question1 = f.encrypt(question1.encode())
            answer1 = f.encrypt(answer1.encode())
            question2 = f.encrypt(question2.encode())
            answer2 = f.encrypt(answer2.encode())
            question3 = f.encrypt(question3.encode())
            answer3 = f.encrypt(answer3.encode())
            question4 = f.encrypt(question4.encode())
            answer4 = f.encrypt(answer4.encode())

            # update the database with the encrypted questions and answers
            SecurityQuestions.objects.filter(user=serializer.data['question1']).update(question1=question1)
            SecurityQuestions.objects.filter(user=serializer.data['answer1']).update(answer1=answer1)
            SecurityQuestions.objects.filter(user=serializer.data['question2']).update(question2=question2)
            SecurityQuestions.objects.filter(user=serializer.data['answer2']).update(answer2=answer2)
            SecurityQuestions.objects.filter(user=serializer.data['question3']).update(question3=question3)
            SecurityQuestions.objects.filter(user=serializer.data['answer3']).update(answer3=answer3)
            SecurityQuestions.objects.filter(user=serializer.data['question4']).update(question4=question4)
            SecurityQuestions.objects.filter(user=serializer.data['answer4']).update(answer4=answer4)
            return Response({'success': 'Security Questions Successfully saved.'}, status=200)
        else:
            return Response({'error': 'Error. Try again'})







# class MyView(views.APIView):

#     def post(self, request):
#         # Get the plaintext data from the form input
#         plaintext = request.data.get('my_field')

#         # Generate a Fernet key
#         key = Fernet.generate_key()

#         # Create a Fernet object with the key
#         f = Fernet(key)

#         # Encrypt the plaintext data
#         ciphertext = f.encrypt(plaintext.encode())

#         # Decrypt the ciphertext data
#         decrypted_plaintext = f.decrypt(ciphertext).decode()

#         # Return the decrypted plaintext data
#         return Response({'decrypted_plaintext': decrypted_plaintext})
