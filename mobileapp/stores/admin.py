from django.contrib import admin
from . import models

# Register your models
admin.site.register(models.Store)
admin.site.register(models.Item)
admin.site.register(models.ItemCategory)
admin.site.register(models.Rating)
