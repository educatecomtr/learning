from django import forms
from project.models import Dealer


# bayiyi ve distribütör ile ilişkilendirme için kullanılmaktadır.
class DealerRelationForm(forms.Form):
    dealer = forms.ModelChoiceField(queryset=Dealer.objects.all())