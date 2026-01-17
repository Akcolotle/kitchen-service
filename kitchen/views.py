from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from kitchen.models import Dish
from kitchen.forms import DishForm

class DishListView(ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type").prefetch_related("cooks")
    template_name = "kitchen/dish_list.html"
    context_object_name = "dish_list"
    paginate_by = 5

class DishDetailView(LoginRequiredMixin, DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("dish-list")
    permission_required = "kitchen.can_manage_dishes"


class DishUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("dish-list")
    permission_required = "kitchen.can_manage_dishes"


class DishDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("dish-list")
    permission_required = "kitchen.can_manage_dishes"