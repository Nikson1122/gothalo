from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from .models import ProfileModel


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    phone_number = forms.RegexField(
    regex=r'^\d+$',  # Only digits
    max_length=15,
    required=True,
    widget=forms.TextInput(attrs={
        'placeholder': 'Enter your phone number',
        'class': 'form-control',
    }),
    error_messages={
        'invalid': 'Enter a valid phone number (digits only).',
    }
)


    class Meta:
        model = User
        fields = ['username' ,'email','phone_number', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        # Adding placeholders for password fields

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter a unique username',
            'class': 'form-control',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter your email address',
            'class': 'form-control',
        })
        
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter a strong password',
            'class': 'form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Re-enter the password',
            'class': 'form-control',
        })


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = ProfileModel
#         fields = ['image',]

#     def __init__(self, *args, **kwargs):
#         super(ProfileUpdateForm, self).__init__(*args, **kwargs)

#         # Adding placeholders for image and phone_number fields
#         self.fields['image'].widget.attrs.update({
#             'placeholder': 'Upload your profile image',
#             'class': 'form-control',
#         })



        # self.fields['phone_number'].widget.attrs.update({
        #     'placeholder': 'Enter your phone number',
        #     'class': 'form-control',
        # })
