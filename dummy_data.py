import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_website.settings")
import django
django.setup()
from faker import factory, Faker
from blog.models import Post
from model_bakery.recipe import Recipe
from django.contrib.auth.models import User

myfake = Faker()

for k in range(20):

    post = Post.objects.get_or_create(title = myfake.sentence(nb_words = 10),
            slug = myfake.slug(),
            description = myfake.sentence(),
            author = User.objects.get(id=1),
            # updated_on = myfake.future_datetime(end_date="+30d", tzinfo=None),
            content = ''.join([f'<p> {paragraph} </p>' for paragraph in [myfake.paragraph(10) for i in range(5)]]),
            # created_on = myfake.future_datetime(end_date="+30d", tzinfo=None),
            status = 1)