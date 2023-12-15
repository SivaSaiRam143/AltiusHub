# Generated by Django 5.0 on 2023-12-15 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test_App', '0002_delete_billsundry'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillSundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billSundryName', models.CharField(max_length=255)),
                ('Amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('invoice_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test_App.header')),
            ],
        ),
    ]