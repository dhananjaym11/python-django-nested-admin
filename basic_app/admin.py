from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import Category, CategoryI18n, Item, ItemI18n


class CategoryI18nTabularInline(NestedTabularInline):
   model = CategoryI18n
   extra = 1


class ItemI18nTabularInline(NestedTabularInline):
   model = ItemI18n
   extra = 1


class ItemStackedInline(NestedStackedInline):
   model = Item
   extra = 1
   inlines = [ItemI18nTabularInline, ]


class CategoryAdmin(NestedModelAdmin):
   inlines = [CategoryI18nTabularInline, ItemStackedInline]


admin.site.register(Category, CategoryAdmin)