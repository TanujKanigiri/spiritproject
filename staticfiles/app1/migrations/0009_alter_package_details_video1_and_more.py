# Generated by Django 5.1.3 on 2025-02-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_package_details_image6_package_details_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_details',
            name='video1',
            field=models.FileField(blank=True, null=True, upload_to='cityvideos/'),
        ),
        migrations.AlterField(
            model_name='package_details',
            name='video2',
            field=models.FileField(blank=True, null=True, upload_to='cityvideos/'),
        ),
        migrations.AlterField(
            model_name='package_details',
            name='video3',
            field=models.FileField(blank=True, null=True, upload_to='cityvideos/'),
        ),
    ]
