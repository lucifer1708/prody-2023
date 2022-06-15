from django import forms
from .models import AddEvent
from django.forms.models import ModelForm


class EventForm(ModelForm):
    event_title = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = AddEvent
        fields = ['event_title', 'name', 'email', 'user', 'event']
