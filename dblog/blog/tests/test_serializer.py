from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
from blog.models import Post, Tag
from blog.serializers import UserSerializer, TagSerializer, PostSerializer

def test_fields():
    assert TagSerializer.Meta.fields == ('pk', 'name')
    assert UserSerializer.Meta.fields == ('pk', 'email', 'first_name', 'last_name')
    assert PostSerializer.Meta.fields == ('pk','title', 'text', 'tags', 'author', 'image')

