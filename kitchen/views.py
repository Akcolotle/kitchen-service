from django.shortcuts import render

from django.views.generic import ListView, DetailView

from kitchen.models import Dish


class DishListView(ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type").prefetch_related("cooks")
    template_name = "kitchen/dish_list.html"
    context_object_name = "dish_list"


class DishDetailView(DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"
