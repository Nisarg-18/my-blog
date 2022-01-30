from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.db.models import Q
# Create your views here.
def blogs(request):
    blogs=Blog.objects.order_by('-created_date')
    data={
        'blogs':blogs,
    }
    return render(request, 'allblogs/blogs.html',data)

def blogdetail(request,id):
    blog=get_object_or_404(Blog, pk=id)
    data={
        'blog':blog,
    }
    return render(request, 'allblogs/blogdetail.html',data)

def search(request):
    blogs=Blog.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            blogs=blogs.filter(Q(title__icontains=keyword)|Q(blog_desc__icontains=keyword))
    data={
        'blogs':blogs,
    }
    return render(request, 'allblogs/search.html', data)
