from django.contrib import admin

from showroom.models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass