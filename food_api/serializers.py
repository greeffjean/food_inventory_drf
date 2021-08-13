from rest_framework import serializers, permissions

from food_client.models import Food

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('name', 'origin')
        # permission_classes = [permissions.IsAuthenticated]

