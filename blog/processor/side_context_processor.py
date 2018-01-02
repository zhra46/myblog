from ..models import *
from django.db.models import Count
def side_context_processor(request):
    c_result = Post.objects.values('category__name','category_id').annotate(count = Count('*')).order_by('-count')[:5]
    tag_result = Post.objects.values('tags__name').annotate(count=Count('*')).order_by('-count')[:5]
    allpost = Post.objects.order_by('-id')
    # created_result = Post.objects.values('created').
    recent = Post.objects.order_by('-id')[:5]
    return{'category_count':c_result,'tag_count':tag_result,'allposts':allpost,'recent':recent}