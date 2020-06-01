from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Default user Serielizer
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'country', 'birth_date',)


class CreateUserSerializer(serializers.ModelSerializer):
    """
    Serializer for create an User model
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'country', 'birth_date', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.username = user.email
        user.set_password(password)
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    """
        Serializer for update an User model
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'country', 'birth_date', 'password')
        extra_kwargs = {}

        @staticmethod
        def update(instance, validated_data):
            email = validated_data.get('email', '')

            if User.objects.exclude(id=instance.id).filter(email=email):
                raise serializers.ValidationError('User with this email already exists.')

            instance.__dict__.update(**validated_data)
            instance.save()

            return instance
