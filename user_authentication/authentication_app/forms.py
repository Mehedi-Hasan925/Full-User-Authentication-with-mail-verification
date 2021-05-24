from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.db.models import fields
from authentication_app import models


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'First Name','class':'mb-2'}))
    last_name = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'mb-2'}))
    email = forms.EmailField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Email','class':'mb-2'}))
    username = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Username','class':'mb-2'}))
    password1 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'mb-2'}))
    password2 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'mb-2'}))
    class Meta:
        model = User
        fields = ('email','first_name','last_name','username','password1','password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Username','class':'mb-3'}))
    password = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'mb-3'}))
    class Meta:
        model = User
        fields = ('username','password')


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'Email','class':'mb-2'}))
    class Meta:
        model = User
        fields = ('email',)

class SetNewPassword(SetPasswordForm):
    new_password1 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'New Password','class':'mb-2'}))
    new_password2 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'mb-2'}))
    class Meta:
        model = User
        fields = ('new_password1','new_password2')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Old Password','class':'mb-2'}))
    new_password1 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'New Password','class':'mb-2'}))
    new_password2 = forms.CharField(required=True, label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'mb-2'}))
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')