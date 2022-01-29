from django.shortcuts import render
from allblogs.models import Blog
# Create your views here.
def home(request):
    blogs=Blog.objects.order_by('-created_date')[:6]
    data={
        'blogs':blogs,
    }
    return render(request, 'webpages/home.html', data)