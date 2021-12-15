from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
        label='نام'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='نام خانوادگی'
    )
    PhoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='موبایل'
    )
    profile = forms.ImageField(
        label='پروفایل'
    )


class UserViewForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام خود را sایید', 'class': 'form-control', 'disabled': 'True',
                   'readonly': 'True'}),
        label='نام'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control', 'disabled': 'True',
                   'readonly': 'True'}),
        label='نام خانوادگی'
    )
    PhoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': "btn btn-primary",
                   'disabled': 'True',
                   'readonly': 'True'}),
        label='پروفایل'
    )
    profile = forms.CharField()
