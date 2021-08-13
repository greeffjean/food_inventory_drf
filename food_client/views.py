from django.shortcuts import render
from food_api.serializers import FoodSerializer
from .models import Food

from rest_framework import viewsets

class FoodViewSet(viewsets.ModelViewSet):
   queryset = Food.objects.all().order_by('name')
   serializer_class = FoodSerializer

def order_food(request):

   return render(request, 'food.html', {})

def update(request):
   foods = Food.objects.all()
   return render(request, 'update.html', {"foods": foods})