from pyexpat import model
import re
from django.contrib import admin
from core.models import *
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','email','first_name','last_name','is_active','date_joined', 'is_staff']
admin.site.register(CustomUser, CustomUserAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id','name','code']
    
admin.site.register(Brand, BrandAdmin)



class GiftAdmin(admin.ModelAdmin):
    list_display = ['id','name','list_products']

    def list_products(self, obj):
        print(obj.product)
        return ", ".join([p.name for p in obj.product.all()])

admin.site.register(Gift, GiftAdmin)

class PercentAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_percent']
admin.site.register(Percent, PercentAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'list_products','description', 'date_start', 'date_stop']
    def list_products(self, obj):
        return ", " .join([p.name for p in obj.product.all()])
admin.site.register(Event, EventAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','code','description']
admin.site.register(Category, CategoryAdmin)

class SizeAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description']
admin.site.register(Size, SizeAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
admin.site.register(Color,ColorAdmin )

class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ['id','code','list_products','description','created_at','update_at']
    def list_products(self, obj):
        return ", " .join([p.name for p in obj.product.all()])
admin.site.register(DiscountCode, DiscountCodeAdmin)

class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['id','time_insurance']
admin.site.register(Insurance, InsuranceAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price','amount','category','created_at']
admin.site.register(Product, ProductAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'rate','comment','created_at']
    
admin.site.register(Review, ReviewAdmin)

class OrderItemAdmin(admin.TabularInline):
    model = Order.product.through

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemAdmin,]
    list_display = ['id','list_products','created_at','status']
    
    def list_products(self, obj):
        print(obj.product)
        return ", ".join([p.name for p in obj.product.all()])

admin.site.register(Order,OrderAdmin)

# admin.site.register(OrderItem)


class CartAdmin(admin.ModelAdmin):
    list_display = ['id','list_orders']

    def list_orders(self, obj):
        return ", " .join([order.user for order in obj.order.all()])
        
admin.site.register(Cart, CartAdmin)




