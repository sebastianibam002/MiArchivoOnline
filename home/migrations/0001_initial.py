# Generated by Django 4.0.4 on 2022-05-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_email', models.EmailField(max_length=254)),
                ('destination_email', models.EmailField(max_length=254)),
                ('generated_url', models.CharField(max_length=50)),
                ('date_sent', models.DateField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
