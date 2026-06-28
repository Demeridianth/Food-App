from django.db import models
from django.conf import settings
from restaurants.models import Restaurant, Dish


# An order should answer these questions:

# Who placed it?
# Which restaurant is it for?
# When was it placed?
# What is its current status?
# What dishes are in it?



class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'pending'
        PREPARING = 'PREPARING', 'preparing'
        ON_THE_WAY = 'ON_THE_WAY', 'on the way'
        DELIVERED = 'DELIVERED', 'delivered'
        CANCELED = 'CANCELED', 'canceled'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    # historical purchase price
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.dish.name}'
