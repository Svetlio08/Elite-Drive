from django.contrib import admin

from catalog.models import Brand, Feature


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass