from crispy_forms.bootstrap import FormActions, StrictButton, FieldWithButtons
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Field
from django.contrib.auth.forms import UserCreationForm
from django import forms
from menu.models import Customer, ShoppingCart, Food
from crispy_forms.helper import FormHelper


class EmailUserCreationForm(UserCreationForm):
    helper = FormHelper()
    helper.form_method="POST"
    helper.add_input(Submit('Register', 'Register', css_class='btn-default'))

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

class FoodQuantityForm(forms.Form):
    food = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(initial=0)

    helper = FormHelper()
    helper.form_method="POST"
    helper.add_input(Submit('add', 'Add', css_class='button white'))
    helper.form_class = 'form-horizontal'
    helper.field_class = 'col-sm-6'
    helper.form_show_labels = False

    helper.layout = Layout(
        # Field('quantity'),
        # FormActions(Submit('add', 'add', css_class='btn-default'))
        # FieldWithButtons('quantity', StrictButton("Test"))
    )