from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars
import PIL as pillow

class ProductCategory(models.Model):

    name = models.CharField(max_length=128, blank=True, null=True, default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

# class ProductManufacturer(models.Model):
#
#     name = models.CharField(max_length=128, blank=True, null=True, default=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return "%s" % self.name
#
#     class Meta:
#         verbose_name = 'Производитель товаров'
#         verbose_name_plural = 'Производители товаров'

class Product(models.Model):

    name = models.CharField(max_length=128, blank=True, null=True, default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=True, on_delete=models.CASCADE)
    # manufacturer = models.ForeignKey(ProductManufacturer, blank=True, null=True, default=True, on_delete=models.CASCADE)
    short_description = models.TextField(max_length=50, blank=True, null=True, default=None,)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def s_description(self):
        return truncatechars(self.description, 30)
    def __str__(self):
            return "%s (%s)" % (self.name, self.price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):

    Product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return "%s" % (self.id)

    class Meta:
        verbose_name = 'Фотография товара'
        verbose_name_plural = 'Фотографии товаров'
