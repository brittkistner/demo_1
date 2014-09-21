from crispy_forms.layout import Submit
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

# class ShoppingCartForm(forms.Form):
#     # food_id = self.fields['fieldname'].widget = HiddenInput()  FINISH
#     food_quantity = forms.IntegerField() #changed something in forms/forms.py
#     # foods
#
#     class Meta:
#         model = ShoppingCart
#         fields = ('quantity', 'foods')

class FoodCountForm(forms.Form):
    food = forms.CharField(max_length=50, widget=forms.HiddenInput())
    quantity = forms.IntegerField(initial=0)

    class Meta:
        model = Food
        fields = ('name')

        #watch video on form and use crispy forms