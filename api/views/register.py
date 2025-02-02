from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..serializers.register import RegisterSerializer

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer