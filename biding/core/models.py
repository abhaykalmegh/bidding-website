from django.db import models
from django.contrib.auth.models import User


class Painting(models.Model):
    painter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    base_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
