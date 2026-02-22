from django.db import models

from catalog.models import Feature, Brand


class Car(models.Model):
    class TransmissionType(models.TextChoices):
        MANUAL = 'M', 'Manual'
        AUTO = 'A', 'Auto'

    class FuelType(models.TextChoices):
        PETROL = 'P', 'Petrol'
        DIESEL = 'D', 'Diesel'
        HYBRID = 'H', 'Hybrid'
        EV = 'E', 'EV'

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )

    model_name = models.CharField(max_length=100)

    year = models.PositiveSmallIntegerField()

    price = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )

    horsepower = models.PositiveSmallIntegerField()

    transmission = models.CharField(
        max_length=10,
        choices=TransmissionType.choices,
    )

    fuel_type = models.CharField(
        max_length=10,
        choices=FuelType.choices,
    )

    image_url = models.URLField(blank=True)

    description = models.TextField(blank=True)

    is_available = models.BooleanField(default=True)

    features = models.ManyToManyField(
        Feature,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)