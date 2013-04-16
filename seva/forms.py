from django import forms
from django.forms.extras.widgets import SelectDateWidget

import account.forms


class SignupForm(account.forms.SignupForm):

    phone = forms.IntegerField(label='Phone', required=True)
    firstname = forms.CharField(label='First Name', required=True)
    lastname = forms.CharField(label='Last Name', required=True)
    phone = forms.IntegerField(label='Year of Study', required=True)
    lastname = forms.CharField(label='Branch', required=True)
    lastname = forms.CharField(label='Blood Group', required=True)
    OPTIONS = (
            ("a", "Animals"),
            ("b", "Arts and Culture"),
            ("b", "Children"),
            ("b", "Education"),
            ("b", "Environment"),
            ("b", "Health"),
            ("b", "Human Rights"),
            ("b", "Hunger"),
            ("b", "Microfinance"),
            ("b", "Women and Girls")
            ) #todo better name to capture form

    focusarea = forms.MultipleChoiceField(label='Focus Area',widget=forms.CheckboxSelectMultiple,
                                         choices=OPTIONS)

    birthdate = forms.DateField(widget=SelectDateWidget(years=range(1910, 2013)))
    remainders = forms.BooleanField(label='Send remainders for the services subscribed')