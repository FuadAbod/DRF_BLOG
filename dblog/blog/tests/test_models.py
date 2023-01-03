# from django.test import TestCase
from blog.models import Post, Tag
import pytest
from conftest import create_post_data

def test_no_post(db):
    assert Post.objects.count() == 0

def test_post(db, create_post_data):
    post_obj = Post.objects.all().values()
    tag_obj = Tag.objects.all().values()
    assert post_obj.count() == 2
    assert tag_obj.count() == 1
    assert post_obj[0] == {'id': 1, 'title': 'LOTR', 'text': 'Active', 'author_id': 1, 'image': ''}
    assert post_obj[1] == {'id': 2, 'title': 'GOT', 'text': 'Inactive', 'author_id': 2, 'image': ''}
    assert tag_obj[0] == {'id': 1, 'name': 'Current Trend'}