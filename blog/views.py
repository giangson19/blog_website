from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
# def home(request):
#     return render(request, 'blog/home.html')

class LatestPostsList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')[:5]
    template_name = 'blog/index.html'

class AllPostsList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'blog/all_posts.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

class About(generic.TemplateView):
    template_name = 'blog/about.html'
    