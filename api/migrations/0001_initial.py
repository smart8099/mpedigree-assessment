# Generated by Django 4.1.2 on 2022-10-18 05:35

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField()),
                ('invoice_items_count', models.IntegerField()),
                ('recipient_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('reference_code', models.CharField(default=api.models.generate_invoice_token, max_length=10, unique=True)),
            ],
        ),
    ]
