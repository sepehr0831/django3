from django import forms
from .models import Post , Category , Comment


#chices = [("coding","coding"),("sport", "sport"),("intertaiment","intertaiment"),]
choices = Category.objects.all().values_list("name", "name")


class PostForm(forms.ModelForm):
    class Meta:



        model = Post

        fields = ("title", "title_tag", "author","category","body","header_image")

        widgets = {

            "title": forms.TextInput(attrs={"class":"form-control"}),
            "title_tag": forms.TextInput(attrs={"class":"form-control"}),
            "author": forms.TextInput(attrs={"class":"form-control", "value":"","id":"sepehr"}),
            "category": forms.Select(choices=[i for i in choices] ,attrs={"class":"form-control"}),
            "body": forms.Textarea(attrs={"class":"form-control"}),


        }



class EditCommentForm(forms.ModelForm):


    class Meta:
        model = Comment

        fields = ("name", "body",)

        widgets = {

            "name": forms.TextInput(attrs={"class":"form-control"}),
            "body": forms.Textarea(attrs={"class":"form-control"}),}