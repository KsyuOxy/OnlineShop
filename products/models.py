from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from subcategories.models import Subcategory


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1024)
    image = models.ImageField(
        null=True,
        blank=True,
        height_field='height_field',
        width_field='width_field',
        upload_to='images/'
    )

    height_field = models.IntegerField(default=0, null=True, blank=True)
    width_field = models.IntegerField(default=0, null=True, blank=True)

    price = models.FloatField(default=0)
    in_stock = models.BooleanField(default=True, null=True, blank=True)
    discount = models.BooleanField(default=False, null=True, blank=True)
    discount_description = models.TextField(default=0, max_length=512, null=True, blank=True)
    discount_price = models.FloatField(default=0, null=True, blank=True)
    discount_percent = models.IntegerField(default=0, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    date_last_sale = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)

    count_of_sold = models.IntegerField(default=0, null=True, blank=True)

    length = models.FloatField(default=0, null=True, blank=True)
    curve = models.CharField(default=0, null=True, blank=True, max_length=15)
    color = models.CharField(default=0, null=True, blank=True,  max_length=25)

    thickness = models.FloatField(default=0, null=True, blank=True)
    coupling_speed = models.FloatField(default=0, null=True, blank=True)
    capacity = models.IntegerField(default=0, null=True, blank=True)

    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp', '-date_last_sale']


def create_slug(instance: Product, new_slug=None) -> str:
    slug = slugify(instance.name)

    if new_slug is not None:
        slug = new_slug

    qs = instance._meta.model.objects.filter(slug=slug).order_by('-id')
    duplicate_exist = qs.exists()

    if duplicate_exist:
        new_slug = f'{slug}-{qs.first().id}'
        return create_slug(instance, new_slug=new_slug)

    return slug


def pre_save_product_receiver(sender, instance: Product, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(receiver=pre_save_product_receiver, sender=Product)
