from django import forms

class CartForm(forms.Form):
    Address = forms.CharField(max_length=100, label='Адрес')
    Number = forms.IntegerField(label='Номер')
    Email = forms.EmailField(label='Эмеил')