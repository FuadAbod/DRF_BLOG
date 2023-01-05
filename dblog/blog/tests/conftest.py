from blog.models import Post
import pytest
from blog.models import Tag
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile
from unittest.mock import MagicMock, patch
from django.core.files import File
from PIL import Image

@pytest.fixture
def create_dummy_data(db):

    tag_1= Tag.objects.create(name="Current Trend")
    tag_1.save()

    author_1 = User.objects.create(username="j", email="j@gmail.com",first_name="John", last_name="elf")
    author_2 = User.objects.create(username="m", email="m@gmail.com", first_name="Raphel", last_name="Don")
    author_1.save()
    author_2.save()
    
    first_post = Post.objects.create(title='LOTR', text='Active', author=author_1, image=None)
    second_post = Post.objects.create(title='GOT', text='Inactive',author=author_2, image= None)
    first_post.save()
    second_post.save()

    first_post.tags.add(tag_1)
    second_post.tags.add(tag_1)

    # return first_post, second_post

@pytest.fixture
def create_api_connection():
    client = APIClient()
    return client