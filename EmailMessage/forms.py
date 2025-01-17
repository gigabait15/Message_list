from django import forms
from .models import EmailMessage, EmailAccount


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class EmailAccountForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = EmailAccount
        fields = '__all__'
        widgets = {
            "client": forms.CheckboxSelectMultiple,
        }
