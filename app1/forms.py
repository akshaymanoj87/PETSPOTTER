from django import forms

class imgForm(forms.Form):
	image=forms.ImageField()