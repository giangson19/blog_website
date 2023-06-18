from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

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
    # content = models.TextField()
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']
        
        
    def __str__(self):
            return self.title