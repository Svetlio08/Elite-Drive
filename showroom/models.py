from django.db import models

from cars.models import Car


class Collection(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    cars = models.ManyToManyField(
        Car,
        related_name='collections',
    )

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)