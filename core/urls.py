from django.urls import path, include
from rest_framework import routers
from core.views import PlotViewSet

router = routers.DefaultRouter()
router.register(r'plot', PlotViewSet)

urlpatterns = [
  
  path('', include(router.urls)),
 
]