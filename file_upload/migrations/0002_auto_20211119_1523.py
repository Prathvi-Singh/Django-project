# Generated by Django 3.2.8 on 2021-11-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='Email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='files',
            name='Roll_no',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='files',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]