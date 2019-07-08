from django.db import models

# Create your models here.
class Category(models.Model):
   private_name = models.CharField('Private name', max_length=164)

   class Meta:
       verbose_name = 'Category'
       verbose_name_plural = 'Categories'


class CategoryI18n(models.Model):
   name = models.CharField('Name i18n', max_length=164)
   category = models.ForeignKey(Category, on_delete=models.PROTECT)

   class Meta:
       verbose_name = 'Category i18n'
       verbose_name_plural = 'Categories i18n'


class Item(models.Model):
   private_name = models.CharField('Private name', max_length=164)
   price = models.DecimalField('Price', decimal_places=2, max_digits=8)
   category = models.ForeignKey(Category, on_delete=models.PROTECT)

   class Meta:
       verbose_name = 'Item'
       verbose_name_plural = 'Items'


class ItemI18n(models.Model):
   name = models.CharField('Name i18n', max_length=164)
   item = models.ForeignKey(Item, on_delete=models.PROTECT)

   class Meta:
       verbose_name = 'Item i18n'
       verbose_name_plural = 'Items i18n'