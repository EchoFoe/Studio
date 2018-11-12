from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


    class ProductCategoryAdmin(admin.ModelAdmin):
        list_display = [field.name for field in ProductCategory._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

        class Meta:
            model = ProductCategory

    admin.site.register(ProductCategory, ProductCategoryAdmin)

# class ProductManufacturerAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductManufacturer._meta.fields]
#     list_filter = ['name', 'id']
#     search_fields = ['name', 'id']
#
#     class Meta:
#         model = ProductManufacturer
#
# admin.site.register(ProductManufacturer, ProductManufacturerAdmin)

class ProductResource(resources.ModelResource):#Делаем отдельный класс ПродуктРесурс, с помощью которого прокидываютя настройки для импорта/экспорта
    category = fields.Field(column_name='category',
                            attribute='category', widget=ForeignKeyWidget(ProductCategory, 'name'))# Т.к. в проекте категория это форейнкей, и мы хотим получить при экспорте название категории, а не его айди, то прописываем эту констуркцию

    class Meta:
        model = Product
        # fields = [field.name for field in Product._meta.fields if field.name != "id"]
        # exclude = ['id']
        # import_id_fields = ['uuid']

class ProductAdmin (ImportExportActionModelAdmin):

    resource_class = ProductResource
    # list_display = [field.name for field in Product._meta.fields if field.name != "id"]
    list_display = ['id', 'name', 'price', 'discount', 'category', 's_description', 'is_active', 'created']
    inlines = [ProductImageInline]
    list_filter = ['category']
    search_fields = ['name', 'id', 'category']

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):

    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)