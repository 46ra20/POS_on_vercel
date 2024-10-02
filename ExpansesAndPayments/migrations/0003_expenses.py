# Generated by Django 5.1.1 on 2024-10-02 13:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpansesAndPayments', '0002_paymentmodel_cash_paymentmodel_company_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_what', models.CharField(default='', max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('cash', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('outstanding', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date', models.DateField(auto_now_add=True)),
                ('expense_by', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]