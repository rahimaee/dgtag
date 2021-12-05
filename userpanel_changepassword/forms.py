from django import forms


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور فعلی خود را وارد کنید'}),
        label='رمز عبور فعلی'

    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز جدید خود را وارد کنید'}),
        label='رمز عبور جدید'

    )
    password_config = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز جدید خود را وارد کنید'}),
        label='تکرار رمز عبور جدید'

    )

    def clean_password_config(self):
        new_password = self.cleaned_data.get('new_password')
        password_config = self.cleaned_data.get('password_config')
        if not new_password == password_config:
            raise forms.ValidationError('رمز عبور با تکرار ان برار نیست')
        return password_config
