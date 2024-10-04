from django.contrib import admin
from .models import Burger, Pizza, Order, Item, Sandwich, Momos
# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL', 'material', 'calories')
admin.site.register(Pizza, PizzaAdmin)
class BurgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL', 'material', 'calories')
admin.site.register(Burger, BurgerAdmin)
class MomosAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'material', 'calories')
admin.site.register(Momos, MomosAdmin)
class SandwichAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'material', 'calories')
admin.site.register(Sandwich, SandwichAdmin)
admin.site.register(Order)
admin.site.register(Item)