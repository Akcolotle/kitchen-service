from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, Dish, DishType


@admin.register(Cook)
class CookAdmin(UserAdmin):
    model = Cook

    list_display = (
        "username",
        "first_name",
        "last_name",
        "years_of_experience",
        "is_staff",
    )
    search_fields = ("username", "first_name", "last_name")

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price")
    search_fields = ("name",)
    list_filter = ("dish_type",)
    filter_horizontal = ("cooks",)