from django.shortcuts import render
from shopApp.models import ProductDB,OrderDB
from shopApp.serializers import ShopSerializer,OrderSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

# Create your views here.
@csrf_exempt
def ShopAPI(request, id=0):
    if request.method == "GET":
        x = ProductDB.objects.all()
        shopserializer = ShopSerializer(x,many=True)
        return JsonResponse(shopserializer.data, safe=False)

    elif request.method == "POST":
        x = JSONParser().parse(request)
        y = ShopSerializer(data=x)
        if y.is_valid():
            y.save()
            return JsonResponse("Data saved sucessfully",safe=False)
        return JsonResponse("Invalid data",safe=False)

    elif request.method == "PUT":
        a = JSONParser().parse(request)
        b = ProductDB.objects.get(ProductId=a['ProductId'])
        serial = ShopSerializer(b, data=a)
        if serial.is_valid():
            serial.save()
            return JsonResponse("Data saved",safe=False)
        return JsonResponse("Invalid data",safe=False)

    elif request.method == "DELETE":
        x = ProductDB.objects.get(ProductId=id)
        x.delete()
        return JsonResponse("data deleted", safe=False)

@csrf_exempt
def OrderAPI(request):
    if request.method == "GET":
        x = OrderDB.objects.all()
        oredr_serializer = OrderSerializer(x,many=True)
        return JsonResponse(oredr_serializer.data, safe=False)

    elif request.method == "POST":
        x = JSONParser().parse(request)
        y = OrderSerializer(data=x)
        if y.is_valid():
            y.save()
            return JsonResponse("Data saved sucessfully", safe=False)
        return JsonResponse("Invalid data", safe=False)


@api_view(['GET'])
def product_list_ordered(request):

    products = OrderDB.objects.annotate(total_orders=Sum('Quantity')).order_by('-total_orders')
    serializer = OrderSerializer(products, many=True)
    return Response(serializer.data)


