from django.forms import ModelForm, TextInput, Textarea, EmailInput

from .models import Contact, Comment, Newsletter


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'type': 'text',
                    'placeholder': 'Your Name',
                    'required': True
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'type': 'email',
                    'placeholder': 'Your Email',
                    'required': True
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'placeholder': 'Message',
                    'style': 'height: 12rem',
                    'required': True
                }
            )
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'text', 'recomment', 'author')
        widgets = {
            'text': TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Your Comment'
                }
            )
        }


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email', )
        
