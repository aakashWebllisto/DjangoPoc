# Generated by Django 4.0.3 on 2022-04-27 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_listing2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('query_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.listing2')),
            ],
        ),
    ]
