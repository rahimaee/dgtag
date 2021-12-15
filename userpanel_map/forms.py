from django import forms

Country_list = ['2', '22', '3']


class MapForm(forms.Form):
    Name = forms.CharField(
        widget=forms.TextInput(),
        label='نام'
    )
    Country = forms.CharField(
        widget=forms.TextInput(),
        label='کشور'
    )

    Province = forms.CharField(
        widget=forms.TextInput(),
        label='استان'
    )
    City = forms.CharField(
        widget=forms.TextInput(),
        label='شهر'
    )
    Address = forms.CharField(
        widget=forms.TextInput(),
        label='ادرس'
    )
    Lat = forms.CharField(
        widget=forms.HiddenInput(),
        label='Lat'
    )
    Lng = forms.CharField(
        widget=forms.HiddenInput(),
        label='Lng'
    )
    MapImg = forms.ImageField()

    MapText = forms.CharField(
        widget=forms.Textarea(),
        label='نقشه'
    )
    DgTag = forms.CharField()
