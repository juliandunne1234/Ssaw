
from django import forms
from .models import Product1, Category1


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product1
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category1.objects.all()
        friendly_names = [(c.id, c.get_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
