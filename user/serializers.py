from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'account_number', 'card_details', 'last_six_digits']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class SecurityQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityQuestions
        fields = ['question1', 'answer1', 'question2', 'answer2', 'question3', 'answer3', 'question4', 'answer4']