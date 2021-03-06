from captcha.fields import CaptchaField
from django import forms
from . import models


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    # widget=forms.PasswordInput用于指定该字段在form表单里表现为
    # <input type='password' />，也就是密码输入框。
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证')
    # class Meta:
    #     model = models.User
    #     fields = ['name', 'password']
    #
    # def __int__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, *kwargs)
    #     self.fields['name'].label = '用户名'
    #     self.fields['password'].label = '密码'


class RegisterForm(forms.Form):
    gender = (
        ('male', '男'),
        ('female', '女')
)
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')
