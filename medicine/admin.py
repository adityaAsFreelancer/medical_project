from django.contrib import admin
from .models import *

# Register your models here.
class itemAdmin(admin.ModelAdmin):
    list_display=('id','iname')
admin.site.register(item,itemAdmin)
class sliderAdmin(admin.ModelAdmin):
    list_display=('id','spic','sdate')
admin.site.register(slider,sliderAdmin)
class itemcategoryAdmin(admin.ModelAdmin):
    list_display=('id','itemname','itempic','itemdiscount')
admin.site.register(itemcategory,itemcategoryAdmin)
