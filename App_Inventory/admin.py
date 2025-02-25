from django.contrib import admin

# Register your models here.
from App_Inventory import models


admin.site.register(models.Attribute)
admin.site.register(models.AttributeTerm)
admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Tag)

admin.site.register(models.Items)

# admin.site.register(models.ItemVariation)

admin.site.register(models.ItemImage)
