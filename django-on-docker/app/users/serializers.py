from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'country', 'birth_date')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'country', 'birth_date')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'country', 'birth_date')
        extra_kwargs = {}

        @staticmethod
        def update(instance, validated_data):
            email = validated_data.get('email', '')

            if User.objects.exclude(id=instance.id).filter(email=email):
                raise serializers.ValidationError('User with this email already exists.')

            instance.__dict__.update(**validated_data)
            instance.save()

            return instance
