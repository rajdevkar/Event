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