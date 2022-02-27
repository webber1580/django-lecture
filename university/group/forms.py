from django import forms


class GroupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Имя' }))
