from django.contrib import admin
from .models import Post, About

# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(About)