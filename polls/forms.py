from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from polls.models import Link


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        data = self.cleaned_data
        data.pop('password2')
        return self.Meta.model.objects.create_user(**data)


class LogInForm(forms.ModelForm):
    phone_or_email = forms.CharField()
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_cache = None


class CreateLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['full']

    def save(self, *args, **kwargs):
        link = super().save(commit=False)
        link.short = self.random_str()
        link.save()
        return link
