from django import forms


class CommentForm(forms.Form):
    FullName = user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input-field borderd', 'id': "name", 'placeholder': 'نام و نام خانوادگی'}),
        label='دیدگاه'

    )
    Email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input-field borderd', 'id': "email", 'placeholder': 'ایمیل'}),
        label='ایمیل'

    )
    Comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'input-field borderd textarea', 'id': 'message', 'placeholder': 'دیدگاه'}),
        label='دیدگاه'
    )
