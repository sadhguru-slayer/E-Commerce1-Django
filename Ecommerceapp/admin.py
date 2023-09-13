from django.contrib import admin
from .models import Contact,Order,OrderUpdate,Brands,Categories,Price_Filter,Product_type,Product,Volume_Filter,Images,Order_item


class Order_itemTube(admin.TabularInline):
    model=Order_item

class Order_admin(admin.ModelAdmin):
    inlines=[Order_itemTube]

# Register your models here.
admin.site.register(Contact)
# admin.site.register(Variant)
admin.site.register(Product)
admin.site.register(OrderUpdate)
admin.site.register(Order,Order_admin)
admin.site.register(Order_item)
admin.site.register(Brands)
admin.site.register(Categories)
admin.site.register(Price_Filter)
admin.site.register(Product_type)
admin.site.register(Volume_Filter)