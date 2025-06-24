from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')

class FileForm(forms.Form):
    xml_file = forms.FileField(label='Selecciona un archivo XML')