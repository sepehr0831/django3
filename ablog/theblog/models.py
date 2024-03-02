from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date
from ckeditor.fields import RichTextField








class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail',args=(str(self.id)) ) or
        #  to come back home page:
        return reverse('home')









class profile(models.Model):
    user = models.OneToOneField(User , null=True ,on_delete=models.CASCADE)
    image=models.ImageField(null=True , blank=True , upload_to= "images/profile/")
    bio = models.TextField()
    website_url = models.CharField(max_length=255 ,null=True ,blank=True)
    insta_url = models.CharField(max_length=255 ,null=True ,blank=True)
    facebook_url = models.CharField(max_length=255 ,null=True ,blank=True)



    def __str__(self):
        return str(self.user)



    def get_absolute_url(self):
        #return reverse('article-detail',args=(str(self.id)) ) or
        #  to come back home page:
        return reverse('home')   








class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, )
    header_image = models.ImageField(null=True , blank=True , upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date  = models.DateField(auto_now_add=True)
    #category = models.ManyToManyField(Category)

    category = models.CharField(max_length=255, default= "uncategorized")
    likes = models.ManyToManyField(User , related_name="blog_posts", blank=True)
    #snippet = models.CharField(max_length=255)



    def total_likes(self):
        return self.likes.count() 


    def __str__(self):
        return  self.title + "   |   " + str(self.author)

    # for working of post button on add post page    
    
    def get_absolute_url(self):
        #return reverse('article-detail',args=(str(self.id)) ) or
        #  to come back home page:
        return reverse('home')



	#<img class="img-fluid" src="{{post.image.url}}" alt="">


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body= models.TextField()
    date_created=models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return  self.post.title + "   |   " + self.name
