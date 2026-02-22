from django.db import models

class Brand(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    country = models.CharField(
        max_length=50,
        blank=True,
    )

    founded_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True,)


class Feature(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(blank=True)