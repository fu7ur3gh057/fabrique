from django.test import TestCase

from apps.client.api.serializers import ClientOutputSerializer


class ClientOutputSerializerTest(TestCase):
    def setUp(self) -> None:
        self.client_data = {
            'operator_code': 999,
            'phone_number': 71234567890,
            'tag': 'Lol',
            'timezone': 'Europe/Moscow',
        }

    def test_client_output_serializer(self) -> None:
        serializer = ClientOutputSerializer(data=self.client_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_validation(self) -> None:
        invalid_data = {
            'operator_code': 999,
            'phone_number': 71234567890,
            'tag': 'Lol',
        }
        serializer = ClientOutputSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('timezone', serializer.errors)
