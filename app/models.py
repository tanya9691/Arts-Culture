from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, View
from .models import Item
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer

import json


def demo(request):
    return render(request, "demo.html")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def item(request):
    return render(request, "item.html")

def payment(request):
    return render(request, "payment.html")

class ItemList(ListView):
    Model = Item
    template_name = "item.html"
    def get_queryset(self):
        item =  Item.objects.all()
        return item

class RegisterationView(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)




# with open("app/products.json") as file:
#     data = json.load(file)
#
#
#     def products(request):
#         try:
#             products = data['products']
#         except KeyError:
#             return None
#         p_id= 1
#
#         for product in products:
#             Name = product.get('name')
#
#         result = {'status': 1, 'message': Name}
#         return JsonResponse(result, safe=False)
#








