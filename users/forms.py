from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class TournamentForm(forms.Form):
   level = forms.CharField(max_length = 20)
   tournament = forms.CharField(max_length = 20)
   gender = forms.CharField(max_length = 20)
   date = forms.DateField()
   venue = forms.CharField(max_length = 60)

class WinnerForm(forms.Form):
   tournament = forms.CharField(max_length = 20)
   gold = forms.CharField(max_length = 100)
   silver = forms.CharField(max_length = 100)
   bronze = forms.CharField(max_length = 100)

class StaffForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(max_length = 100)