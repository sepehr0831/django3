from django.contrib.auth.forms import UserCreationForm , UserChangeForm  ,  PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields =("bio","image","website_url","insta_url","facebook_url",)

        widgets = {

                "bio": forms.Textarea(attrs={"class":"form-control"}),
                #"image": forms.ImageField(attrs={"class":"form-control"}),
                "website_url": forms.TextInput(attrs={"class":"form-control"}),
                "insta_url": forms.TextInput(attrs={"class":"form-control"}),
                "facebook_url": forms.TextInput(attrs={"class":"form-control"}),


            }





class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model= User
        fields=("username","first_name","last_name","email", "password1", "password2")
    #for good loking of username and password1 in reginster page
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"





class EditProfileFrom(UserChangeForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100 , widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=100 , widget=forms.CheckboxInput(attrs={'class': 'form-Check'}))
    is_staff = forms.CharField(max_length=100 , widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=100 , widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': 'form-control'}))



    class Meta:
        model= User
        fields=("username","first_name","last_name","email", "is_superuser",  "is_active","is_staff","last_login", "date_joined" , "password") 




class passwordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100 ,widget=forms.PasswordInput(attrs={'class': 'form-control', "type":"password"}))
    new_password1 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class': 'form-control' ,"type":"password"}))
    new_password2 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class': 'form-control' ,"type":"password"}))

    class Meta:
        model= User
        fields=("old_password","new_password1","new_password2")




class EditProfilePageFrom(forms.ModelForm):

    class Meta:
        model = profile
        fields =("bio","image","website_url","insta_url","facebook_url",)

        widgets = {

                "bio": forms.Textarea(attrs={"class":"form-control"}),
                #"image": forms.ImageField(),
                "website_url": forms.TextInput(attrs={"class":"form-control"}),
                "insta_url": forms.TextInput(attrs={"class":"form-control"}),
                "facebook_url": forms.TextInput(attrs={"class":"form-control"}),


            }