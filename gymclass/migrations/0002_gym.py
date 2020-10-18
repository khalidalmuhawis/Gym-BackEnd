# Generated by Django 3.1.2 on 2020-10-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymclass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('openningtime', models.TimeField()),
                ('closingtime', models.TimeField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]