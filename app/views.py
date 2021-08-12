from django.shortcuts import render
from .models import Order, Item
from .serializers import OrderSerializer, ItemSerializer
from rest_framework import generics 





class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

