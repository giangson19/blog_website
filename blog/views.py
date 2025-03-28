from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, About, Comment, Subscriber
from django.views import generic
from .forms import CommentForm


# Create your views here.
# def home(request):
#     return render(request, 'blog/home.html')

class LatestPostsList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')[:5]
    template_name = 'blog/index.html'

class AllPostsList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'blog/all_posts.html'
    paginate_by = 5

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments = Comment.objects.filter(
            post=self.get_object()).order_by('-created')
        data['comments'] = comments
        # if self.request.user.is_authenticated:
        data['comment_form'] = CommentForm()

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'),
                                  name=request.POST.get('name'),
                                
                                  post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class About(generic.DetailView):
    model = About
    template_name = 'blog/about.html'
    
    def get_object(self):
        return self.model.objects.get(pk=1)
    
def Schedule(request): 
    return render(request, 'blog/schedule.html')

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        subscriber, created = Subscriber.objects.get_or_create(email=email)

        if not created and subscriber.is_active:
            messages.warning(request, "You are already subscribed.")
        else:
            subscriber.is_active = True
            subscriber.save()
            messages.success(request, "Thank you for subscribing!")

    return redirect(request.META.get('HTTP_REFERER', 'homepage'))