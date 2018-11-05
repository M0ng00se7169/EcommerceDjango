import math

from django.db import models
from django.db.models.signals import pre_save, post_save

from billing.models import BillingProfile
from myApp.utils import unique_order_id_generator
from carts.models import Cart

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded')
)


class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        order_qs = self.get_queryset().filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        created = False
        if order_qs.count() == 1:
            obj = order_qs.first()
        else:
            obj = self.model.objects.create(billing_profile=billing_profile, cart=cart_obj)
            created = True
        return obj, created


# Create your models here.
class Order(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=False, null=True, blank=True)
    order_id        = models.CharField(max_length=120, blank=True)
    cart            = models.ForeignKey(Cart, on_delete=False)
    status          = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total  = models.DecimalField(default=5.99, max_digits=20, decimal_places=2)
    order_total     = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    active          = models.BooleanField(default=True)

    def __unicode__(self):
        return self.order_id

    objects = OrderManager()

    def update_total(self):
        cart_total = math.fsum([self.cart.total, 0])
        shipping_total = self.shipping_total
        new_total = math.fsum([cart_total, shipping_total])
        self.order_total = new_total
        self.save()
        return new_total


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)


pre_save.connect(pre_save_create_order_id, sender=Order)


def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()


post_save.connect(post_save_cart_total, sender=Cart)


def post_save_order(sender, instance, created, *args, **kwargs):
    print('running')
    if created:
        print('Updating... first')
        instance.update_total()


post_save.connect(post_save_order, sender=Order)
