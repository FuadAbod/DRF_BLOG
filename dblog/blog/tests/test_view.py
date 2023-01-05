from conftest import create_api_connection,create_dummy_data
from django.urls import reverse
import pytest
from django.core import serializers
import json
from unittest.mock import patch

@pytest.mark.django_db
def test_get_request_method(create_dummy_data, create_api_connection):
    get_request = create_api_connection.get('/api/posts')
    assert get_request.status_code == 200
    assert get_request.json()[0] == {'pk': 1, 'title': 'LOTR', 'text': 'Active', 'tags': [{'pk': 1, 'name': 'Current Trend'}], 'author': {'pk': 1, 'email': 'j@gmail.com', 'first_name': 'John', 'last_name': 'elf'}, 'image': None}
    assert get_request.json()[1] == {'pk': 2, 'title': 'GOT', 'text': 'Inactive', 'tags': [{'pk': 1, 'name': 'Current Trend'}], 'author': {'pk': 2, 'email': 'm@gmail.com', 'first_name': 'Raphel', 'last_name': 'Don'}, 'image': None}
    
@pytest.mark.django_db
def test_post_request_method(create_dummy_data, create_api_connection):
    body_request= {'title': 'LOTR', 'text': 'Inactive', 'image': None}
    post_request = create_api_connection.post('/api/posts',data=body_request, format="json")
    assert post_request.json() == {'pk': 3, 'title': 'LOTR', 'text': 'Inactive', 'tags': [], 'author': None, 'image': None}

@pytest.mark.django_db
def test_put_request_method(create_dummy_data, create_api_connection):

    body_request = {
        'title':"LOTR",
        'text': 'InActive'
    }
    put_request = create_api_connection.put('/api/posts/1/', data= body_request, format="json")
    assert put_request.json()['text'] == "InActive"


@pytest.mark.django_db
def test_delete_request_method(create_dummy_data, create_api_connection):
    delete_request = create_api_connection.delete('/api/posts/1/', format="json")
    assert delete_request.status_code == 204

    


    
    