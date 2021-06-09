from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()

router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
