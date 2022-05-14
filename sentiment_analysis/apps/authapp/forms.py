from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


# class ShopUserLoginForm(AuthenticationForm):
#
#     def get_invalid_login_error(self):
#         return forms.ValidationError(
#             self.error_messages['invalid_login'],
#             code='invalid_login',
#             params={'username': 'телефон'},
#         )
#
#     class Meta:
#         model = ShopUser
#         fields = ('phone', 'password')
#
#     def __init__(self, *args, **kwargs):
#         super(ShopUserLoginForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username']:
#             self.fields[fieldname].label = 'Телефон (+7)'
#         for field_name, field in self.fields.items():
#
#             if field_name == 'username':
#                 field.widget.attrs['maxlength'] = 10
#                 field.widget.attrs['minlength'] = 10
#
#             field.widget.attrs['class'] = 'form-control'
#
#             if field_name == 'password':
#                 field.widget.attrs['minlength'] = 8


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget.attrs['minlength'] = 8

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
