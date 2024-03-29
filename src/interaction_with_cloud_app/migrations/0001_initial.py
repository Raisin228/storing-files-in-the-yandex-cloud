# Generated by Django 5.0.1 on 2024-02-06 13:29

import interaction_with_cloud_app.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnyFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_name', models.CharField(max_length=50, unique=True)),
                ('relative_url_image', interaction_with_cloud_app.models.YandexImageField(
                    storage=interaction_with_cloud_app.models.YandexStorage(),
                    upload_to=interaction_with_cloud_app.models.user_directory_path_by_images,
                    verbose_name='Your Image')),
                ('abs_image_url', models.URLField(blank=True, editable=False)),
                ('relative_url_file', interaction_with_cloud_app.models.YandexFileField(
                    storage=interaction_with_cloud_app.models.YandexStorage(),
                    upload_to=interaction_with_cloud_app.models.user_directory_path_by_files,
                    verbose_name='Your File')),
                ('abs_file_url', models.URLField(blank=True, editable=False)),
            ],
        ),
    ]
