from django import forms
from .models import SignUp

class SingUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        emailbase,provider = email.split('@')
        domain,extension = provider.split('.')
        if not '.edu' in email:
            raise forms.ValidationError("Use valide college email")
        return email
    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name

