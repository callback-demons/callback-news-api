"""Categories views."""
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import CreateUserSerializer, UpdateUserSerializer, UserSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CreateUserView(CreateAPIView):
    """
    A viewset that provides the standard actions for create User Model.
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UpdateUserView(UpdateAPIView):
    """
    An endpoint for update the user fields.
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
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})