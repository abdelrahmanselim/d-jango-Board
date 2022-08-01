from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Div,Layout

from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    post_pictures = forms.ImageField()
    content = forms.CharField(max_length=1000)

