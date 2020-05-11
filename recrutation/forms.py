from django import forms
from .models import RecruitmentModel


class RecruitmentForm(forms.ModelForm):
    presentation = forms.CharField(label="Opisz siebie", widget=forms.Textarea)
    full_name = forms.CharField(label="Imię i nazwisko")

    class Meta:
        model = RecruitmentModel
        fields = ['full_name', 'email', 'presentation']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        if "pw.edu.pl" not in provider:
            raise forms.ValidationError("Napisz e-mail PW ")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
