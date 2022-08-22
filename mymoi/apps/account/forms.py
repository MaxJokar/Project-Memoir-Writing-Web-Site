from django import forms
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'family','mobile_number','gender')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField(help_text="To change Password , <a href ='../password'>Click Here </a> ")

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'family','mobile_number','gender', 'is_active', 'is_admin')


# Common User Be able to register , log on with restriction
Choice_Gender=(("True","man"),("False","woman"))
class RegisterUserForm(forms.Form):
    email = forms.EmailField(label = "",
                             error_messages={'required':'This field is necessary',
                             'invalid':'This email is ivalid'},
                            widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'email'}))
    name = forms.CharField(label=""
                           , widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'Name'}))
    family =forms.CharField(label="",
                            error_messages={'required ':'This field is necessary'}
                            , widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'Family'}))
    mobile_number = forms.CharField(label="",
                                    error_messages={'required':'This field is necessary'}
                                    , widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'Mobile Number'}))
    gender = forms.ChoiceField(label="", choices=Choice_Gender,
                               )
    password = forms.CharField(label="",
                               error_messages={'required':'This field is necessary'}
                               ,widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'password'}))


    confirm_password = forms.CharField(label="",
                               error_messages={'required':'This field is necessary'}
                               ,widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'confirm password'}))





    def clean_email(self):  # sourcery skip: use-named-expression
        email=self.cleaned_data['email']
        flag = CustomUser.objects.filter(email=email).exists()
        if flag :
            raise ValidationError('This email was registered BEFORE')
        return email



    def clean_mobile_number(self):  # sourcery skip: use-named-expression
        email=self.cleaned_data['mobile_number']
        flag = CustomUser.objects.filter(mobile_number=mobile_number).exists()
        if flag :
            raise ValidationError('This email was registered BEFORE')
        return mobile_number



    def clean(self):  # sourcery skip: use-named-expression
        email=self.cleaned_data('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password and confirm_password and password!=confirm_password :
            raise ValidationError('password & confirm are not THE SAME')
        return email




class LoginUserForm(forms.Form):
    email = forms.EmailField(label = "",
                             error_messages={'required':'This field is necessary'}
                            ,widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'email'}))
    password = forms.CharField(label="",
                               error_messages={'required':'This field is necessary'}
                               ,widget=forms.TextInput(attrs={'class':'form_control', 'placeholder':'password'}))
