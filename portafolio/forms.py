from django import forms

class contactForm(forms.Form):
    Full_name = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'full name or company name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'email'}))
    contact_message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'message'}))