from django.urls import path , include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Products/',ProductViewSet, basename = 'Products')



urlpatterns = router.urls
