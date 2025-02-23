from django import forms
from .models import Feedback
from django.core.exceptions import ValidationError

def validate_email_domain(value):
    if not value.endswith('@example.com'):
        raise ValidationError('Only @example.com emails are allowed.')

class FeedbackForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_email_domain])

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 50:
            raise ValidationError('Feedback message must be at least 50 characters long.')
        return message
