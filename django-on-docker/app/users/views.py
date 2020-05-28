"""Categories views."""
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import CreateUserSerializer, UpdateUserSerializer, UserSerializer

class CreateUserView(CreateAPIView):
    """
        A viewset that provides the standard actions for create User Model.
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class UpdateUserView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = UpdateUserSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj



class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for User Model.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
