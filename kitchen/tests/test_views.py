from django.test import TestCase
from django.urls import reverse
from kitchen.models import Dish, DishType, Cook


class DishViewTests(TestCase):
    def setUp(self):
        self.manager = Cook.objects.create_user(
            username="manager",
            password="testpass",
        )

        content_type = ContentType.objects.get_for_model(Dish)
        permission = Permission.objects.get(
            codename="can_manage_dishes",
            content_type=content_type,
        )

        self.manager.user_permissions.add(permission)

        self.cook = Cook.objects.create_user(
            username="cook",
            password="cookpass",
        )

        self.dish_type = DishType.objects.create(name="Soup")
        self.dish = Dish.objects.create(
            name="Borch",
            price=100,
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_dish_list_view(self):
        response = self.client.get(reverse("dish-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
        self.assertIn(self.dish, response.context["dish_list"])

    def test_dish_detail_view(self):
        response = self.client.get(
            reverse("dish-detail", kwargs={"pk": self.dish.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_detail.html")
        self.assertEqual(response.context["dish"], self.dish)

    def test_dish_create_view(self):
        self.client.login(username="manager", password="testpass")

        response = self.client.post(
            reverse("dish-create"),
            {
                "name": "Borch",
                "description": "Ukrainian soup",
                "price": "100.00",
                "dish_type": self.dish_type.id,
                "cooks": [self.cook.id],
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="Borch").exists())

    def test_dish_update_view(self):
        self.client.login(username="manager", password="testpass")

        response = self.client.post(
            reverse("dish-update", args=[self.dish.id]),
            {
                "name": "Updated Borch",
                "description": "Updated description",
                "price": "120.00",
                "dish_type": self.dish_type.id,
                "cooks": [self.cook.id],
            },
        )

        self.assertEqual(response.status_code, 302)

        self.dish.refresh_from_db()

        self.assertEqual(self.dish.name, "Updated Borch")

        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, "Updated Borch")

    def test_dish_delete_view(self):
        self.client.login(username="manager", password="testpass")

        response = self.client.post(
            reverse("dish-delete", args=[self.dish.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())
