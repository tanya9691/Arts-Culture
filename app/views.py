import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, View
from .models import Item
<<<<<<< HEAD
=======





#from rest_framework import generics
#from rest_framework.response import Response
#from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import UserSerializer, UserLoginSerializer, UserLogoutSerializer

>>>>>>> f55920776b120d4707a1b639a1add59bfa3d9850
import json

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def demo(request):
    return render(request, "demo.html")

def index1(request):
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

# class RegisterationView(generics.ListCreateAPIView):
#     # get method handler
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
<<<<<<< HEAD
#
=======

>>>>>>> f55920776b120d4707a1b639a1add59bfa3d9850
# class LoginView(generics.GenericAPIView):
#     # get method handler
#     queryset = User.objects.all()
#     serializer_class = UserLoginSerializer
<<<<<<< HEAD
#
=======

>>>>>>> f55920776b120d4707a1b639a1add59bfa3d9850
#     def post(self, request, *args, **kwargs):
#         serializer_class = UserLoginSerializer(data=request.data)
#         if serializer_class.is_valid(raise_exception=True):
#             return Response(serializer_class.data, status=HTTP_200_OK)
#         return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
<<<<<<< HEAD
#
#
# class LogoutView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserLogoutSerializer
#
=======


# class LogoutView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserLogoutSerializer

>>>>>>> f55920776b120d4707a1b639a1add59bfa3d9850
#     def post(self, request, *args, **kwargs):
#         serializer_class = UserLogoutSerializer(data=request.data)
#         if serializer_class.is_valid(raise_exception=True):
#             return Response(serializer_class.data, status=HTTP_200_OK)
#         return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
<<<<<<< HEAD
#
#
=======


>>>>>>> f55920776b120d4707a1b639a1add59bfa3d9850


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








