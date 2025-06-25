from django.shortcuts import render
from .models import Post, About
from django.views import generic


# Create your views here.
# def home(request):
#     return render(request, 'blog/home.html')

class LatestPostsList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')[:5]
    template_name = 'blog/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get total count of published posts
        context['post_count'] = Post.objects.filter(status = 1).count()
        return context

class AllPostsList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'blog/all_posts.html'
    # paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_count'] = self.queryset.count()
        return context
    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
    
class AboutView(generic.DetailView):
    model = About
    template_name = 'blog/about.html'
    
    def get_object(self):
        return self.model.objects.get(pk=1)
