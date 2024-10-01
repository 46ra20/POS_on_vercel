from django.contrib import admin
from .models import CategoryModel,ProductModel,BrandModel,UnitModel,PurchaseModel
# Register your models here.


class SlugFieldAddBrand(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand",)}

class SlugFieldAddCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category",)}
class SlugFieldUnit(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("unit",)}


admin.site.register(CategoryModel,SlugFieldAddCategory)
admin.site.register(BrandModel,SlugFieldAddBrand)
admin.site.register(UnitModel,SlugFieldUnit)
admin.site.register(ProductModel)
admin.site.register(PurchaseModel)
