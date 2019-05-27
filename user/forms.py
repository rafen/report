from datetime import date

from allauth.account.forms import SignupForm
from django import forms

from .models import User


class UserForm(forms.ModelForm):
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(date.today().year - 80, date.today().year - 15))
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'birthday', 'picture',
            'address_line_1', 'address_line_2', 'phone', 'city', 'state', 'zip',
            'country', 'language'
        )


class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
