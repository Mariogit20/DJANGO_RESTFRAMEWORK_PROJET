from django.contrib import admin
from .models import Produits
# Register your models here.
class DashProduit(admin.ModelAdmin):
    list_display = ('nom','description','prix','image')

admin.site.register(Produits,DashProduit)