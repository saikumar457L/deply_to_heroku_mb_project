from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView

from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = "posts/home.html"
    #context_object_name = "all_posts_list"
