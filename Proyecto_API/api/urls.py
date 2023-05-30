from rest_framework import routers
from .api import VarViewSet
from django.urls import path
from .views import VariablesView

router = routers.DefaultRouter()

router.register('api/variables',VarViewSet, 'api')

urlpatterns = router.urls
