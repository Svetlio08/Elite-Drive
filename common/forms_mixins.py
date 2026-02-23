class BootstrapFormMixin:

    def _bootstrap_fields(self):
        for field in self.fields.values():
            widget = field.widget
            widget_name = widget.__class__.__name__

            if widget_name in ("CheckboxInput",):
                widget.attrs["class"] = "form-check-input"
            elif widget_name in ("Select", "SelectMultiple"):
                widget.attrs["class"] = "form-select"
            else:
                widget.attrs["class"] = "form-control"