from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from categories.models import Category


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(
        null=True,
        blank=True,
        height_field='height_field',
        width_field='width_field',
        upload_to='images/'
    )
    height_field = models.IntegerField(default=0, null=True, blank=True)
    width_field = models.IntegerField(default=0, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name


def create_slug(instance: Subcategory, new_slug=None) -> str:
    slug = slugify(instance.name)

    if new_slug is not None:
        slug = new_slug

    qs = instance._meta.model.objects.filter(slug=slug).order_by('-id')
    duplicate_exist = qs.exists()

    if duplicate_exist:
        new_slug = f'{slug}-{qs.first().id}'
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_subcategory_receiver(sender, instance: Subcategory, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(receiver=pre_save_subcategory_receiver, sender=Subcategory)
