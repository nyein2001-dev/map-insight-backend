# Generated by Django 5.1 on 2024-08-31 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('name_en', models.CharField(max_length=255)),
                ('name_mm', models.CharField(max_length=255)),
                ('road_en', models.CharField(blank=True, max_length=255, null=True)),
                ('road_mm', models.CharField(blank=True, max_length=255, null=True)),
                ('township_en', models.CharField(max_length=255)),
                ('township_mm', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('agency_id', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=6)),
                ('shape', models.JSONField()),
                ('stops', models.ManyToManyField(related_name='routes', to='dashboard.stop')),
            ],
        ),
    ]
