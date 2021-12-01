from django import forms


class NewslettersForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', }),
        label='ایمیل',

    )
