from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label = "Name", max_length = 80)
    check = forms.BooleanField(required = False)
