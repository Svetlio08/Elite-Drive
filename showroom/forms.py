from django import forms

from common.forms_mixins import BootstrapFormMixin
from .models import Collection


class CollectionForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Collection
        fields = ["title", "description", "cars", "is_featured"]
        labels = {"title": "Collection title", "is_featured": "Featured"}
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Hypercars 2026"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Optional description..."}),
        }
        help_texts = {
            "cars": "Select cars to include in this collection.",
        }
        error_messages = {
            "title": {"required": "Please enter a collection title."},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap_fields()

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title


class CollectionDeleteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Collection
        fields = ["title", "description", "is_featured", "cars"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap_fields()
        for f in self.fields.values():
            f.disabled = True