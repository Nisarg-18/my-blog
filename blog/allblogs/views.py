from django.shortcuts import render, get_object_or_404
from .models import Blog
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