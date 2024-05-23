from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import File, Product

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if user is None:
            raise serializers.ValidationError("User does not exist")
        if not user.check_password(data['password']):
            raise serializers.ValidationError("Incorrect password")
        return data
    
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = ('user', 'uploaded_at', 'file_type', "name")


class ArithmeticSerializer(serializers.Serializer):
    num1 = serializers.FloatField()
    num2 = serializers.FloatField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class DummySerializer(serializers.Serializer):
    pass