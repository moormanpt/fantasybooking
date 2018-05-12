import floppyforms as forms
from parsley.decorators import parsleyfy
from django.forms import widgets
from django.forms import ModelForm
from django import forms
from fantasybooking.home.models import Stable, Wrestler, WeeklyStat


class StripeTokenForm(forms.Form):
    id = forms.CharField()


class ChargeForm(forms.Form):
    amount = forms.DecimalField(max_digits=5, decimal_places=2)


@parsleyfy
class UserForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=30, help_text="Type your full name")
    email = forms.EmailField(help_text="Enter your email address")
    age = forms.IntegerField(help_text="Enter your age")

    def clean_name(self):
        if(len(self.data['name']) < 5):
            raise forms.ValidationError("Is your name really that short?")
        if(len(self.data['name'].split(' ')) < 2):
            raise forms.ValidationError("Your full name please.")

    def good_to_go(self):
        pass

class StableForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    
    class Meta:
        model = Stable
        fields = "__all__" 

class WrestlerForm(forms.ModelForm):
    wrestler = Wrestler.objects.get(pk=1)

    class Meta:
        model = Wrestler
        fields = ['name', 'stable']
