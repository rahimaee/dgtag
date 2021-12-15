from django import forms


class UserNewOrderForm(forms.Form):
    productId = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )


class AddressForm(forms.Form):
    country = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'}),
        label='کشور'
    )
    province = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'استان'}),
        label='استان'
    )
    city = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'}),
        label='شهر'
    )
    FullAddress = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کامل'}),
        label='ادرس کامل'
    )
    ZipCode = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی'}),
        label='کد پستی'
    )
