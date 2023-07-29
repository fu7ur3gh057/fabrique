import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from apps.distribution.models import Distribution

api_client = APIClient()


@pytest.fixture
def create_distribution() -> Distribution:
    return Distribution.objects.create(
        start_time='2023-07-26 16:19:26.757+04',
        end_time='2023-07-28 16:19:26.757+04',
        text='Hello brother',
        filter=['Lol']
    )


@pytest.fixture
def create_distributions() -> list[Distribution]:
    d1 = Distribution.objects.create(
        start_time='2023-07-26 16:19:26.757+04',
        end_time='2023-07-28 16:19:26.757+04',
        text='Hello brother',
        filter=['Lol']
    )
    d2 = Distribution.objects.create(
        start_time='2023-07-26 13:20:26.757+04',
        end_time='2023-07-28 14:05:25.757+04',
        text='Yo wassup',
        filter=['994']
    )
    return [d1, d2]


@pytest.mark.django_db
def test_distribution_list(create_distributions) -> None:
    url = reverse('distribution-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_update_distribution(create_distribution) -> None:
    sample_data = {'text': 'Hello mate'}
    url = reverse('distribution-update', args=[create_distribution.pk_id])
    response = api_client.patch(url, data=sample_data)
    assert response.status_code == 200
    assert Distribution.objects.all().first().text == sample_data['text']


@pytest.mark.django_db
def test_delete_distribution(create_distribution) -> None:
    url = reverse('distribution-delete', args=[create_distribution.pk_id])
    response = api_client.delete(url)
    assert response.status_code == 200
    assert Distribution.objects.count() == 0

# @pytest.mark.django_db
# def test_statistic_distribution() -> None:
#     pass
#
#
# @pytest.mark.django_db
# def test_detail_statistic_distribution() -> None:
#     pass
