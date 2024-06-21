from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm, PasswordChangeForm
from django import forms

from catalog.form import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserRecoveryForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ("email",)


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
