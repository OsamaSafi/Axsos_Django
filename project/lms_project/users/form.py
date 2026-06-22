from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'id': 'confirmPassword',
        }),
        label="Confirm Password"
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
            'password',
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'firstName',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'lastName',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-2',
                'id': 'email',
                'placeholder': 'name@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'id': 'phone',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control mb-2',
                'id': 'password',
            }),
            
            'birthday': forms.DateInput(attrs={
                'class': 'form-control mb-2',
                'id': 'birthday',
                'type': 'date'
            }),
        }


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        
        confirm_password = self.data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("must both passwords are match!")
            
        return cleaned_data
    

class LoginForm(forms.Form): 
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-2',
            'id': 'email',
            'placeholder': 'name@example.com'
        }),
        label="Email"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'id': 'password',
        }),
        label="Password"
    )