from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('foods/', views.foods, name='foods'),
    path('foods/<int:id>', views.get_food, name='get_foods'),
    path('update/', views.update, name='get_foods'),
    path('create_food/', views.create_food, name='create_food'),
    path('delete_food/<int:id>', views.del_food, name='delete_food'),
    path('update_food/<int:id>', views.update_food, name='update_food'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
