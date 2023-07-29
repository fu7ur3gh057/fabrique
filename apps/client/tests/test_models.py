from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.client.models import Client


class ClientModelTest(TestCase):
    def setUp(self) -> None:
        self.client = Client.objects.create(
            operator_code=999,
            phone_number=71234567890,
            tag='Lol',
            timezone='Europe/Moscow'
        )

    def test_client_creation(self) -> None:
        self.assertTrue(isinstance(self.client, Client))
        self.assertEqual(self.client.operator_code, 999)
        self.assertEqual(self.client.phone_number, 71234567890)
        self.assertEqual(self.client.tag, 'Lol')
        self.assertEqual(self.client.timezone, 'Europe/Moscow')

    def test_operator_code_len_not_equal_3(self) -> None:
        with self.assertRaises(ValidationError) as context:
            self.client.operator_code = 3
            self.client.save()
            self.client.full_clean()
        self.assertTrue('length of operator_code should be equal 3' in str(context.exception))

    def test_phone_number_not_starts_with_7(self) -> None:
        with self.assertRaises(ValidationError) as context:
            self.client.phone_number = 12345678900
            self.client.save()
            self.client.full_clean()
        self.assertTrue('The value must start with 7.' in str(context.exception))

    def test_phone_number_len_not_equal_11(self) -> None:
        with self.assertRaises(ValidationError) as context:
            self.client.phone_number = 12345
            self.client.save()
            self.client.full_clean()
        self.assertTrue('length of phone_number should be equal 11' in str(context.exception))

    def test_timezone_validation(self) -> None:
        with self.assertRaises(ValidationError) as context:
            self.client.timezone = 'Lol'
            self.client.save()
            self.client.full_clean()
        self.assertTrue('Invalid timezone' in str(context.exception))
