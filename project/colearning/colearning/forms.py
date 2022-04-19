from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label = "Title", max_length = 80)
    message = forms.CharField(label = "Content", max_length = 250)
    sender = forms.EmailField()
    notification_needed = forms.BooleanField(required = False)
