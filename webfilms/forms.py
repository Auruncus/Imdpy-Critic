from django import forms

from webfilms.models import MovieRating

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', max_length=1024, widget=forms.PasswordInput)

class RateMovieForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    rating = forms.IntegerField(min_value=0, max_value=5)
