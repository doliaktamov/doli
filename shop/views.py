from django.shortcuts import render
from .serializers import CategorySerializer, ItemSerializer
from .models import Category, Item
from rest_framework import authentication, permissions
from rest_framework.viewsets import ModelViewSet

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]


class ItemViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]