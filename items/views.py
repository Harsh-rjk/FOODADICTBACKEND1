from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Items
from .serializers import ItemSerializer

def items(request):
    return HttpResponse("hey this is my items section")




# ✅ GET all items
@api_view(['GET'])
def get_items(request):
    items = Items.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# ✅ POST new item
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
