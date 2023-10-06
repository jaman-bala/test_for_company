from django.contrib import admin
from .models import Category, City, Advert


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'city',
        'category',
        'created',
        'views',
    )
    search_fields = (
        'title',
    )


admin.site.site_header = 'Панель администрирования'