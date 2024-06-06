from django import forms
from .models import Country, Currency

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"


class CurrencyForm(forms.ModelForm):
    country = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
    # country = forms.ModelChoiceField(queryset=Country.objects.all())

    class Meta:
        model = Currency
        fields = '__all__'
