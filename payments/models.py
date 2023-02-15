from django.db import models


class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item for item in self.items.all())


class Item(models.Model):
    order = models.ManyToManyField(Order, related_name='items')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, default='usd')

    def __str__(self):
        return f'Item {self.id}'

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


