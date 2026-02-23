from django import forms
from django.utils import timezone

from common.forms_mixins import BootstrapFormMixin
from .models import Brand, Feature


class BrandForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "country", "founded_year"]
        labels = {"name": "Brand name", "founded_year": "Founded year"}
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. Ferrari"}),
            "country": forms.TextInput(attrs={"placeholder": "e.g. Italy"}),
            "founded_year": forms.NumberInput(attrs={"placeholder": "e.g. 1939"}),
        }
        error_messages = {
            "name": {
                "required": "Please enter a brand name.",
                "unique": "This brand already exists.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap_fields()

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Brand name must be at least 2 characters long.")
        return name

    def clean_founded_year(self):
        year = self.cleaned_data.get("founded_year")
        if year is None:
            return year
        current_year = timezone.now().year
        if year < 1800 or year > current_year:
            raise forms.ValidationError(f"Founded year must be between 1800 and {current_year}.")
        return year


class BrandDeleteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "country", "founded_year"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap_fields()
        for f in self.fields.values():
            f.disabled = True


class FeatureForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Feature
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. Carbon Package"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Optional description..."}),
        }
        error_messages = {
            "name": {
                "required": "Please enter a feature name.",
                "unique": "This feature already exists.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap_fields()

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Feature name must be at least 2 characters long.")
        return name


class FeatureDeleteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Feature
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap_fields()
        for f in self.fields.values():
            f.disabled = True