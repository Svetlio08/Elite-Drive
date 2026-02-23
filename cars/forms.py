from django import forms
from django.utils import timezone

from common.forms_mixins import BootstrapFormMixin
from .models import Car


class CarCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "brand", "model_name", "year", "price", "horsepower",
            "transmission", "fuel_type", "image_url", "description",
            "is_available", "features",
        ]
        labels = {
            "model_name": "Model",
            "image_url": "Image URL",
            "is_available": "Available",
        }
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Short description..."}),
            "image_url": forms.URLInput(attrs={"placeholder": "https://..."}),
            "model_name": forms.TextInput(attrs={"placeholder": "e.g. Aventador SVJ"}),
        }
        help_texts = {
            "features": "Optional: select luxury features.",
        }
        error_messages = {
            "model_name": {"required": "Please enter a model name."},
            "year": {"required": "Please enter a year."},
            "price": {"required": "Please enter a price."},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap_fields()

    def clean_year(self):
        year = self.cleaned_data["year"]
        current_year = timezone.now().year
        if year < 1950 or year > current_year + 1:
            raise forms.ValidationError(f"Year must be between 1950 and {current_year + 1}.")
        return year

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    def clean_horsepower(self):
        hp = self.cleaned_data["horsepower"]
        if hp <= 0:
            raise forms.ValidationError("Horsepower must be a positive number.")
        return hp

    def clean_model_name(self):
        name = self.cleaned_data["model_name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Model name must be at least 2 characters long.")
        return name


class CarEditForm(CarCreateForm):
    created_at = forms.DateTimeField(label="Created at", disabled=True, required=False)

    class Meta(CarCreateForm.Meta):
        fields = CarCreateForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["created_at"].initial = self.instance.created_at


class CarDeleteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = ["brand", "model_name", "year", "price", "horsepower", "transmission", "fuel_type"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap_fields()
        for f in self.fields.values():
            f.disabled = True