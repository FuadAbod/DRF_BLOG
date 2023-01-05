from conftest import create_api_connection
from django.urls import reverse

def test_urls(create_api_connection):
    test_create_and_read_url = reverse('api-cr')
    test_update_and_delete_url = reverse('api-ud', args=[1])
    assert test_create_and_read_url == '/api/posts'
    assert test_update_and_delete_url == '/api/posts/1/'