# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import *
from haystack.backends import SQ
from haystack.query import SearchQuerySet

from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def get_blog_bp(page_num):
    paginator = Paginator(Post.objects.order_by('-id'),1)
    return paginator.page(page_num)
def get_page_list(page):
    page_num = int(page.number)
    max_page=page.paginator.num_pages
    start = page_num-3
    end = page_num+4
    if start<1:
        start=1
        if start+7>max_page:
            end=max_page+1
        else:
            end=start+7
    if end > max_page:
        end =max_page+1
        start = end - 7
        if start <1:
            start=1
    return range(start,end)

class IndexView(View):
    def get(self,request,page_num=None):
        if not page_num:
            return HttpResponseRedirect('/blog/page/1')
        print(request.path)
        post_page = get_blog_bp(page_num)
        print post_page.has_previous()
        post = post_page.object_list[0]
        paginator_list = get_page_list(post_page)
        print paginator_list
        print(post.__dict__)
        return render(request, 'index/index.html', {'ppost':post_page, 'post':post, 'plist':paginator_list, 'page_num':page_num})

class DetailsView(View):
    def get(self,request,blog_id = None):
        if blog_id:
            post = Post.objects.get(id=blog_id)
            print post.content
            return render(request, 'details/details.html',{'post':post} )
        else:
            raise Http404


class CategoryDetails(View):
    def get(self,request,category_id = None):
        if category_id:
            posts = Post.objects.filter(category__id=category_id).order_by('-id')
            print(posts)
            return render(request,'categories/details.html',{'cposts':posts})


class ArchiveDetails(View):
    def get(self,request,year=None,month=None):
        if not year or not month:
            aposts = Post.objects.order_by('-id')
        else:
            year = int(year)
            month = int(month)
            aposts = Post.objects.filter(created__startswith='%s-%s'%(year,month)).order_by('-id')
        return render(request,'archive/details.html',{'aposts':aposts})


class MakePost(View):
    pass


class Search(View):
    def get(self,request):
        kw = request.GET.get('q','')
        print kw
        result = SearchQuerySet().filter(SQ(title=kw)|SQ(content=kw)).all()
        posts = [post.object for post in result]
        print posts
        return render(request,'archive/details.html',{'aposts':posts})