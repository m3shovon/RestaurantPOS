from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import uuid
from .models import Category, Items

@receiver(pre_save, sender=Category)
def generate_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        if Category.objects.filter(slug=instance.slug).exists():
            instance.slug = f"{instance.slug}-{uuid.uuid4().hex[:8]}"

@receiver(pre_save, sender=Items)
def generate_item_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        if Items.objects.filter(slug=instance.slug).exists():
            instance.slug = f"{instance.slug}-{uuid.uuid4().hex[:8]}"