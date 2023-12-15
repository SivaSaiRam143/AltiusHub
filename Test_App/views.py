from rest_framework import viewsets, authentication, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404


class HeaderViewSet(viewsets.ModelViewSet):

    serializer_class = HeaderSerializer
    queryset = Header.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK) 
    
    def create(self, request, *args, **kwargs):
        
        header_serializer = self.get_serializer(data=request.data)
        if header_serializer.is_valid():
            header_obj = header_serializer.save()
        else:
            return Response(data=header_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        items_data = request.data['items']
        item_objs = []
        for item_data in items_data:
            item_data['Amount'] = item_data['Quantity']*item_data['Price']
            item_obj, _ = Item.objects.get_or_create(invoice_header=header_obj, **item_data)
            item_objs.append(item_obj.id)
        request.data['items'] = item_objs
        temp = sum([float(x['Amount']) for x in items_data]) + sum([float(x['Amount']) for x in request.data['billsundry']])
        sundrys_data = request.data['billsundry']
        sundry_objs = []
        for sundry_data in sundrys_data:
            sundry_obj, _ = Item.objects.get_or_create(invoice_header=header_obj, **sundry_data)
            sundry_objs.append(sundry_obj.id)
        request.data['billsundry'] = sundry_objs
        request.data['TotalAmount'] = temp
        return Response(data=header_serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request,  pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        items_data = list(Item.objects.filter(invoice_header=instance).values("itemName", "Quantity", "Price", "Amount"))
        sundry_data = BillSundry.objects.filter(invoice_header=instance).values("billSundryName", "Amount")
        data['Items'] = items_data
        data['billsundry'] = sundry_data
        return Response(data=serializer.data, status=status.HTTP_200_OK) 

    def update(self, request,  pk=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        self.perform_update(serializer)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request,  pk=None, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

































# def login_view(request):
#     if request.method == "POST":
#         user_name = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=user_name, password=password)
#         if user:
#             login(request, user)
#             return redirect("home")
#     elif request.method == "GET":
#         return render(request, "Test_App/login.html", {})


# @login_required
# def logout_view(request):
#     logout(request=request)
#     return redirect("login")

    