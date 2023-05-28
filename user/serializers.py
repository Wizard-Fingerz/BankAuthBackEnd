from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'account_number', 'card_details', 'last_six_digits', 'email', 'password']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'profile_image']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AnswerSerializer(serializers.Serializer):
    question = serializers.CharField()
    answer = serializers.CharField()
    encryption_key = serializers.CharField()

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)


class SecurityQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityQuestions
        fields = ['question1', 'answer1', 'question2', 'answer2', 'question3', 'answer3', 'question4', 'answer4']
