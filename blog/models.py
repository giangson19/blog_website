from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
import readtime

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length = 300)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', default='giangson')
    updated_on = models.DateTimeField(auto_now= True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']
    
    def get_readtime(self):
        result = readtime.of_html(self.content)
        return result.text + ' read'
    
    def __str__(self):
            return self.title
        
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()
        
class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = HTMLField()
    
    def save(self, *args, **kwargs):
        # if not self.pk and About.objects.exists():
        # if you'll not check for self.pk 
        # then error will also be raised in the update of exists model
            # raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(About, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
# class Comment(models.Model):
#     blogpost_connected = models.ForeignKey(
#         Post, related_name='comments', on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = TextField()
#     date_posted = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return str(self.author) + ', ' + self.blogpost_connected.title[:40]
    
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'