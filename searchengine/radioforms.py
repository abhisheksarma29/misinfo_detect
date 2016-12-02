from django import forms

class RadioForm(forms.form):
    input1 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    input2 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    input3 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

