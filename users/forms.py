from allauth.account.forms import SignupForm, LoginForm
from django import forms


class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=30, label='First Name')
    phone_number = forms.CharField(max_length=12, label='Phone Number')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
