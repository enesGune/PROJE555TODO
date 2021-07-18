from django import forms
from .models import Customer


class CustomerForms(forms.ModelForm):
    tc_no = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'TC NUMARASI'}))
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'AD'}))
    surname = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'SOYAD'}))
    phone_number = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'TELEFON NO'}))
    city = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'İL'}))
    town = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'İLÇE'}))

    class Meta:
        model = Customer
        fields = [
            'tc_no',
            'name',
            'surname',
            'phone_number',
            'city',
            'town',
        ]

    def clean_tc_no(self, *args, **kwargs):
        tc_no = self.cleaned_data.get('tc_no')
        if len(tc_no) < 11:
            raise forms.ValidationError('Geçerli Bir Tc Numarası Değildir')
        else:
            return tc_no
