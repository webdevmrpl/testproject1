from django import forms
from .models import Bb
from django.forms.widgets import EmailInput


class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'img', 'rubric')
        labels = {'title': 'Название товара'}
        help_texts = {'rubric': 'Выберите рубрику'}
        field_classes = {'price': forms.DecimalField}


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(min_length=8, max_length=30, widget=forms.widgets.PasswordInput(render_value=False))
    email = forms.EmailField(widget=EmailInput)
