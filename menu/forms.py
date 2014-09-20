from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from menu.models import Customer


class EmailUserCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )