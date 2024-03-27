from django import forms
from django.forms import formset_factory

class imgForm(forms.Form):
	image   = forms.ImageField()