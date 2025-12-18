from django.contrib import admin

from kitchen.models import Cook, Dish, DishType


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "years_of_experience",
        "is_staff",
    )
    search_fields = ("username", "first_name", "last_name")


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price")
    search_fields = ("name",)
    list_filter = ("dish_type",)
    filter_horizontal = ("cooks",)
