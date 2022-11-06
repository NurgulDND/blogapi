from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_auth.views import LoginView, LogoutView
from rest_framework.filters import SearchFilter

from . import serializers
from .permissions import IsAccountOwner


class CustomLoginView(LoginView):
    permission_classes = (permissions.AllowAny,)


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserListView(generics.ListAPIView): # список юзеров
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserListSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('username', 'email')



class UserDetailView(generics.RetrieveAPIView): #детальная информация о юзере
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsAccountOwner)


class UserRegisterView(generics.CreateAPIView): #Регистрация
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = (permissions.AllowAny,)

