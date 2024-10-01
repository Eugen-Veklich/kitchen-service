from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import IntegerField


class DishType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    quantity = IntegerField()

    def __str__(self):
        return self.name, self.quantity


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.username


class Dish(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cook = models.ManyToManyField(Cook, null=True)
    ingredients = models.ManyToManyField(Ingredient, null=True)

    def __str__(self):
        return self.name
