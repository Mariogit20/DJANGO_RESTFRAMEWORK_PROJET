from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProduitViewSet
# r: m'eviter ilay antislas 
router = DefaultRouter()
router.register (r'produits',ProduitViewSet) #mampiseho anleizy

urlpatterns = [
    path('',include(router.urls))
]