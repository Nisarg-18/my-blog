from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.blogs,name="blogs"),
    path('<int:id>',views.blogdetail,name="blogdetail"),
]