# Generated by Django 2.1 on 2018-09-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20180828_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieslist',
            name='MovieImage',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
