from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status

from food_api.serializers import FoodSerializer
from .models import Food

from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return render(request, 'food.html', {})


@api_view(['GET'])
def foods(request):
    queryset = Food.objects.all().order_by('name')
    serializer = FoodSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_food(request, id):
    try:
        query = Food.objects.get(pk=id)
        serializer = FoodSerializer(query)
        return Response(serializer.data)

    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_food(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def del_food(request, id):
    try:
        Food.objects.get(pk=id).delete()
    except ModuleNotFoundError as e:
        return Response(e)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def update_food(request, id):
    query = Food.objects.get(pk=id)
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        print('is_valid')
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update(request):
    foods = Food.objects.all()
    return render(request, 'update.html', {"foods": foods})
