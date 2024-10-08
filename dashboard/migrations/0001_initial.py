from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=50)),
                ('insight', models.TextField(blank=True, max_length=500)),
                ('url', models.URLField(blank=True, max_length=500)),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('relevance', models.IntegerField(blank=True, null=True)),
                ('pestle', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('likelihood', models.IntegerField(blank=True, null=True)),
                ('intensity', models.IntegerField(blank=True, null=True)),
                ('added', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
