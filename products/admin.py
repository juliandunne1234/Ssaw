from django.contrib import admin
from .models import Product1, Category1


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'category',
        'name',
        'photographer',
        'price',
        )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )


admin.site.register(Product1, ProductAdmin)
admin.site.register(Category1, CategoryAdmin)
