# Generated by Django 3.1.7 on 2021-04-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210417_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='addinfo',
            name='developer_rating',
            field=models.FloatField(default='developer_rating', max_length=50),
        ),
        migrations.AddField(
            model_name='addinfo',
            name='score',
            field=models.FloatField(default='score', max_length=50),
        ),
    ]