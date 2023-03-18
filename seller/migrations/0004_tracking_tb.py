# Generated by Django 4.1.4 on 2023-01-11 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_order_tb'),
        ('seller', '0003_product_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='tracking_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=20)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.order_tb')),
            ],
        ),
    ]