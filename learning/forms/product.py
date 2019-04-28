from django.forms import ModelForm, Textarea
from learning.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

