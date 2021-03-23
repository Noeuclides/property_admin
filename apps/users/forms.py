from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.users.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
    
class RegisterForm(forms.ModelForm):
   
    password1 = forms.CharField(label = 'password',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'password',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Confirm password', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = User
        fields = ('email','id_card','name','last_name')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Email',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Last name',
                }                
            ),
            'id_card': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ID CARD',
                }
            )
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user