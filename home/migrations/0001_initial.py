# Generated by Django 3.1.7 on 2021-04-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=30)),
                ('design', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
    ]
