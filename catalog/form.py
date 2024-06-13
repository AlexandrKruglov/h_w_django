from django.forms import ModelForm, BooleanField
from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ("name_product", "description", "image", "category", "prise", "created_at", "updated_at")

    def clean_name_product(self):
        cleaned_data = self.cleaned_data['name_product']
        #stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in self.stop_word:
            if word in cleaned_data.lower():
                raise forms.ValidationError('поменяйте имя продукта')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        #stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in self.stop_word:
            if word in cleaned_data.lower():
                raise forms.ValidationError('в описании запрещенные слова')

        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
