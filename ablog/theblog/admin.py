from django.contrib import admin
from .models import Post , Category , profile , Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(profile)
admin.site.register(Comment)


