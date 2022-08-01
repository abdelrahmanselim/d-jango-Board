from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    descreption = models.CharField(max_length=200)
    def __str__(self):
        return self.name;
class Post(models.Model):
    title=models.CharField(max_length=100)
    created_by=models.ForeignKey(User,related_name='post_user', on_delete=models.CASCADE)
    post_pictures=models.ImageField( upload_to='board/images', null=True)
    content=models.CharField(max_length=10000)
    category=models.ForeignKey(Category,related_name='post_category', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title;
    def get_new_post_url(self):
        return reverse('newpost',args=[self.category.pk])

class Comment(models.Model):
    comment=models.CharField(max_length=500)
    post=models.ForeignKey(Post, related_name='post_cat', on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment;
