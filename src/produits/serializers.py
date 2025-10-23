from rest_framework import serializers
from .models import Produits
# ito noho api ampifandraisana azy
class ProduitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produits
        fields = '__all__'
