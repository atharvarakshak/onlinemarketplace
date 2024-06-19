from django.urls import reverse
from django.test import RequestFactory
import pytest

from .views import index, contact, signup
from .models import Category, Item

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.mark.django_db
def test_index_view(request_factory):
    # Create some sample data
    category = Category.objects.create(name='Test Category')
    item = Item.objects.create(name='Test Item', is_sold=False, category=category)

    # Create a request
    request = request_factory.get(reverse('index'))

    # Call the view function
    response = index(request)

    # Check that the response is successful
    assert response.status_code == 200

    # Check that the template contains the expected data
    assert category.name.encode() in response.content
    assert item.name.encode() in response.content

@pytest.mark.django_db
def test_contact_view(request_factory):
    # Create a request
    request = request_factory.get(reverse('contact'))

    # Call the view function
    response = contact(request)

    # Check that the response is successful
    assert response.status_code == 200

@pytest.mark.django_db
def test_signup_view_get(request_factory):
    # Create a request
    request = request_factory.get(reverse('signup'))

    # Call the view function
    response = signup(request)

    # Check that the response is successful
    assert response.status_code == 200

@pytest.mark.django_db
def test_signup_view_post(request_factory):
    # Create a POST request with valid form data
    form_data = {
        'username': 'testuser',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }
    request = request_factory.post(reverse('signup'), data=form_data)

    # Call the view function
    response = signup(request)

    # Check that the user is redirected to the login page
    assert response.status_code == 302
    assert response.url == '/login'
