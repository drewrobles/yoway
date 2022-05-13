from django.db import models


class Order(models.Model):
    food = models.ManyToManyField('Food')
    name = models.CharField(max_length=45)
    instructions = models.TextField(max_length=95)

    def __str__(self):
        return f'{self.name} {self.instructions}'


class Food(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.name}'