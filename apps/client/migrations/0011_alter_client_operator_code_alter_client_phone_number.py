# Generated by Django 4.1.10 on 2023-07-26 12:00

import apps.client.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_alter_client_operator_code_alter_client_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='operator_code',
            field=models.IntegerField(help_text='Введите значение из 3 цифр.', validators=[apps.client.validators.validate_three_digits]),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.BigIntegerField(default=70000000000, unique=True, validators=[apps.client.validators.validate_starts_with_7, apps.client.validators.validate_ten_digits]),
        ),
    ]
