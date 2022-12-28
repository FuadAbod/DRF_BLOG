# from django.test import TestCase
from blog.models import Post, Tag
import pytest
from conftest import create_post_data
def test_no_post(db):
    assert Post.objects.count() == 0

def test_post(db,create_post_data):
    data= create_post_data[0]

    # assert create_post_data.objects.count() == 2
#     assert Post_creation.objects.active.count() == 1
#     assert Post_creation.objects.inactivet.count() == 1

# def test_no_tag():
#     assert Tag.objects.count == 0
#     assert Tag.objects.count() == 1