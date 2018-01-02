# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
import datetime
# class Manager_bo(models.Manager):
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(null=True, blank=True)
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(upload_to='static/img/%s/'%datetime.date.today(),null=True,blank=True,)
    def __unicode__(self):
        return self.title
class Comment(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    Post = models.ForeignKey('Post')
    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

if __name__ == '__main__':
    post= Post.objects.first()
    print(post.tag.objects)
