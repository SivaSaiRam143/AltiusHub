from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class HeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Header
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    
    invoice_header = HeaderSerializer()

    class Meta:
        model = Item
        fields = "__all__"

class BillSundrySerializer(serializers.ModelSerializer):
     
    invoice_header = HeaderSerializer()
     
    class Meta:
        model = BillSundry
        fields = "__all__"