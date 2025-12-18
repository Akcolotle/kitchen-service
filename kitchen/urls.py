from django.urls import path

from kitchen.views import DishListView

urlpatterns = [
    path("dishes/", DishListView.as_view(), name="dish-list"),
]