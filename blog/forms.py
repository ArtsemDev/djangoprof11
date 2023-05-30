from django import forms

from blog.models import Contact


class ContactForm(forms.ModelForm):
    username = forms.TextInput()
    email = forms.EmailInput()
    message = forms.Textarea()

    class Meta:
        model = Contact
        fields = ('username', 'email', 'message')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'username',
                    'placeholder': 'Enter your name'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'placeholder': 'Enter your email'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'placeholder': 'Enter your message',
                    'style': 'height: 12rem'
                }
            )
        }
