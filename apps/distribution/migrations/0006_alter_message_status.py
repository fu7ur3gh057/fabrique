# Generated by Django 4.1.10 on 2023-07-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0005_alter_message_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('ERROR', 'Error'), ('SUCCESS', 'Success'), ('EXPIRED', 'Expired')], default='ERROR', max_length=10),
        ),
    ]