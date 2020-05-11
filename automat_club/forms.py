from django import forms


class ContactForm(forms.Form):
    nazwa = forms.CharField(label="Przedstaw się:", required=False)
    email = forms.EmailField()
    tresc = forms.CharField(label="Treść", widget=forms.Textarea)
