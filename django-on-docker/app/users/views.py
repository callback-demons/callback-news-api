"""Categories views."""
from rest_framework import permissions, viewsets
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """
        A viewset that provides the standard actions for Categories Model.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for User Model.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
