from blog.models import Post
from unittest.mock import MagicMock
import pytest
from blog.models import Tag
from django.contrib.auth.models import User

@pytest.fixture
def create_post_data(db):
    tag_1= Tag.objects.create(name="Current Trend")
    tag_1.save()

    author_1 = User(username="j", email="j@gmail.com")
    author_2 = User(username="m", email="m@gmail.com")
    author_1.save()
    author_2.save()
    
    first_post = Post.objects.create(title='LOTR', text='Active', author=author_1)
    second_post = Post.objects.create(title='GOT', text='Inactive',author=author_2)
    first_post.save()
    second_post.save()

    first_post.tags.add(tag_1)
    second_post.tags.add(tag_1)
    
    return first_post, second_post
    