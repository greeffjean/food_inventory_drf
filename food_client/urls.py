from . import views
from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()
router.register(r'food', views.FoodViewSet)

urlpatterns = [
    path('', views.order_food, name='index'),
    path('update/', views.update, name='update'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
