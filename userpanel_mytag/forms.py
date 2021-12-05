from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Fieldset, HTML, ButtonHolder, Submit
from django.contrib.auth.models import User

from mytag_cards.models import Card
from django import forms
from django.forms.models import inlineformset_factory

from mytag_cards_contactnumbers.models import ContactNumbers
from mytag_cards_socialnetworks.models import SocialNetwork
from userpanel_mytag.custom_layout_object import Formset


#
# # class CardForm(forms.ModelForm):
# #     class Meta:
# #         model = Card
# #         widgets = {
# #             'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
# #             'LastName': forms.TextInput(attrs={'class': 'form-control'}),
# #             'Company': forms.TextInput(attrs={'class': 'form-control'}),
# #             'WorkName': forms.TextInput(attrs={'class': 'form-control'}),
# #             'Bio': forms.Textarea(attrs={'class': 'form-control'}),
# #             'UserName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
# #
# #         }
# #
# #         fields = (
# #             'ProfileImg',
# #             'FirstName',
# #             'LastName',
# #             'Company',
# #             'WorkName',
# #             'Bio',
# #             'UserName',
# #         )
# #
# #
# # class ContactNumbersForm(forms.ModelForm):
# #     class Meta:
# #         model = ContactNumbers
# #         fields = ('Name', 'Number', 'Type')
# #         widgets = {
# #             'Name': forms.TextInput(attrs={'class': 'form-control'}),
# #             'Number': forms.TextInput(attrs={'class': 'form-control'}),
# #             'Type': forms.Select(attrs={'class': 'form-control'}),
# #
# #         }
# #
# #
# # CardFormset = inlineformset_factory(
# #     Card,
# #     ContactNumbers,
# #     form=ContactNumbersForm,
# #     extra=5,
# #     # max_num=5,
# #     # fk_name=None,
# #     # fields=None, exclude=None, can_order=False,
# #     # can_delete=True, max_num=None, formfield_callback=None,
# #     # widgets=None, validate_max=False, localized_fields=None,
# #     # labels=None, help_texts=None, error_messages=None,
# #     # min_num=None, validate_min=False, field_classes=None
# #
# # )
# #
#
# class ContactNumbersForm(forms.ModelForm):
#     class Meta:
#         model = ContactNumbers
#         exclude = ()
#         fields = (
#             'Name',
#             'Number',
#             'Type'
#         )
#         widgets = {
#             'Name': forms.TextInput(attrs={'class': 'form-control'}),
#             'Number': forms.TextInput(attrs={'class': 'form-control'}),
#             'Type': forms.Select(attrs={'class': 'form-control'}),
#
#         }
#
#
# # class SocialNetworkForm(forms.ModelForm):
# #     class Meta:
# #         model = SocialNetwork
# #         exclude = ()
# #         fields = (
# #             'Name',
# #             'Url',
# #             'Type',
# #
# #         )
# #         widgets = {
# #             'Name': forms.TextInput(attrs={'class': 'form-control'}),
# #             'Url': forms.TextInput(attrs={'class': 'form-control'}),
# #             'Type': forms.Select(attrs={'class': 'form-control'}),
# #
# #         }
#
#
# class CardForm(forms.ModelForm):
#     class Meta:
#         model = Card
#         exclude = ['created_by', ]
#         fields = (
#             'ProfileImg',
#             'FirstName',
#             'LastName',
#             'Company',
#             'WorkName',
#             'Bio',
#             'UserName',
#         )
#
#     def __init__(self, *args, **kwargs):
#         super(CardForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = True
#         self.helper.form_class = 'role="form"'
#         self.helper.label_class = 'col-md-3 create-label'
#         self.helper.field_class = 'form-group'
#         self.helper.layout = Layout(
#
#             # Div(
#             #     Field('ProfileImg'),
#             #     Field('FirstName'),
#             #     Field('LastName'),
#             #     Field('Company'),
#             #     Field('Bio'),
#             #     Field('UserName'),
#             # Fieldset('شماره ها', Formset('titles')),
#             #     # HTML("<br>"),
#             #     ButtonHolder(Submit('submit', 'دخیره')),
#             # ),
#             Div(
#                 Div(
#                     Field('ProfileImg'),
#                     css_class='form-group'
#                 ),
#                 Div(
#                     Field('FirstName', css_class='form-control'),
#                     css_class='form-group'
#                 ),
#                 Div(
#                     Field('LastName', css_class='form-control'),
#                     css_class='form-group'
#                 ),
#                 Div(
#                     Field('Company', css_class='form-control'),
#                     css_class='form-group'
#                 ),
#                 Div(
#                     Field('Bio'),
#                     css_class='form-group'
#                 ),
#                 Div(
#                     Field('UserName'),
#                     css_class='form-group'
#                 ),
#                 Div(
#                     Fieldset('شماره ها', Formset('titles')),
#                     css_class='form-group'
#                 ),
#                 # Div(
#                 #     Fieldset('شماره ها', Formset('cards')),
#                 #     css_class='form-group'
#                 # ),
#                 ButtonHolder(Submit('submit', 'دخیره')),
#             )
#
#         )
#
#
# CardFormset = inlineformset_factory(
#     Card,
#     ContactNumbers,
#     form=ContactNumbersForm,
#     fields=['Name', 'Number', 'Type'],
#     extra=2,
#     # can_delete=True,
# )
#
# # CardSocialNetworkFormset = inlineformset_factory(
# #     Card,
# #     SocialNetwork,
# #     form=SocialNetworkForm,
# #     fields=['Name', 'Url', 'Type'],
# #     extra=2,
# #     # can_delete=True,
# # )


class ContactNumbersForm(forms.ModelForm):
    class Meta:
        model = ContactNumbers
        exclude = ()


ContactNumbersFormSet = inlineformset_factory(
    Card, ContactNumbers, form=ContactNumbersForm,
    fields=['Name', 'Number', 'Type'], extra=3, can_delete=False
)


class CardSocialNetworkForm(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        exclude = ()


CardSocialNetworkFormset = inlineformset_factory(
    Card, SocialNetwork, form=CardSocialNetworkForm,
    fields=['Name', 'Url', 'Type'], extra=3, can_delete=False
)


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        widgets = {
            'FirstName': forms.TextInput(attrs={'class': 'form-control'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control'}),
            'Company': forms.TextInput(attrs={'class': 'form-control'}),
            'WorkName': forms.TextInput(attrs={'class': 'form-control'}),
            'Bio': forms.Textarea(attrs={'class': 'form-control'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
        }

        fields = ('ProfileImg', 'FirstName', 'LastName', 'Company', 'WorkName', 'Bio', 'UserName')
        exclude = ['created_by', ]

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-md-3 create-label'
        # self.helper.field_class = 'col-md-9'
        
        self.helper.layout = Layout(
            Div(
                Field('ProfileImg'),
                Field('FirstName'),
                Field('LastName'),
                Field('Company'),
                Field('WorkName'),
                Field('Bio'),
                Field('UserName'),
                Fieldset('شبکه های اجتماعی',
                         Formset('cards')),
                Fieldset('شماره ها',
                         Formset('titles')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'ذخیره')),
            )
        )
