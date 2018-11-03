from django.db import models

from carts.models import Cart

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)


# Create your models here.
class Order(models.Model):
    order_id       = models.CharField(max_length=120, blank=True)
    cart           = models.ForeignKey(Cart, on_delete=False)
    status         = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99, max_digits=20, decimal_places=2)
    order_total    = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

    def __unicode__(self):
        return self.order_id
