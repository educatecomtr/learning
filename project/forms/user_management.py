from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class StaffCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Ad')
    last_name = forms.CharField(label='Soyad')
    email = forms.EmailField(label='Email')


class StaffUpdateForm(forms.ModelForm):

    edit_password = forms.CharField(label='Şifre', widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'edit_password', 'email')


class StaffPermissionForm(forms.Form):
    product_permission = forms.BooleanField(label='Ürün Yönetimi', required=False)
    dealer_permission = forms.BooleanField(label='Bayi Yönetimi', required=False)
    order_permission = forms.BooleanField(label='Sipariş Yönetimi', required=False)
    payment_permission = forms.BooleanField(label='Ödeme Yönetimi', required=False)
