from rest_framework import serializers
from shopApp.models import ProductDB,OrderDB

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDB
        fields = (
            'ProductName',
            'Description',
            'Size',
            'Color',
            'Status'
    )

class OrderSerializer(serializers.ModelSerializer):
     class Meta:
         model = OrderDB
         fields = [
             'ProductId',
             'Quantity',
         ]
