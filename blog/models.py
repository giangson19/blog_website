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