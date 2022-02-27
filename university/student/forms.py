from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Имя' }))
    surname = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Фамилия' }))
    age = forms.IntegerField(widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Возраст' }))
    group_id = forms.IntegerField(widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Номер группы' }))