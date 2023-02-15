from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, default='usd')

    def __str__(self):
        return f'Item {self.id}'

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


