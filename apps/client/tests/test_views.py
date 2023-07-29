import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from apps.client.models import Client

api_client = APIClient()


@pytest.fixture
def create_client() -> Client:
    return Client.objects.create(
        operator_code=333,
        phone_number=71234567890,
        tag='Lol',
        timezone='Europe/London'
    )


@pytest.fixture
def create_clients() -> list[Client]:
    c1 = Client.objects.create(
        operator_code=333,
        phone_number=71234567890,
        tag='Lol',
        timezone='Europe/London'
    )
    c2 = Client.objects.create(
        operator_code=333,
        phone_number=72222567890,
        tag='Olo',
        timezone='Europe/London'
    )
    return [c1, c2]


# Client List Test
@pytest.mark.django_db
def test_client_list(create_clients) -> None:
    url = reverse('client-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


# Client Create Test
@pytest.mark.django_db
def test_create_client() -> None:
    sample_data = {
        'operator_code': 333,
        'phone_number': 71234567890,
        'tag': 'Lol',
        'timezone': 'Europe/London'
    }
    url = reverse('client-create')
    response = api_client.post(url, data=sample_data)
    assert response.status_code == 201
    assert Client.objects.count() == 1


# Client Update Test
@pytest.mark.django_db
def test_update_client(create_client) -> None:
    sample_data = {'operator_code': 999}
    url = reverse('client-update', args=[create_client.pk_id])
    response = api_client.patch(url, data=sample_data)
    assert response.status_code == 200
    assert Client.objects.all().first().operator_code == sample_data['operator_code']


# Client Delete Test
@pytest.mark.django_db
def test_delete_client(create_client) -> None:
    url = reverse('client-delete', args=[create_client.pk_id])
    response = api_client.delete(url)
    assert response.status_code == 200
    assert Client.objects.count() == 0
