# Generated by Django 3.2.6 on 2021-08-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('dateTime', models.DateTimeField(verbose_name='DateTime')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('image', models.CharField(max_length=1024, verbose_name='ImageURL')),
                ('college', models.CharField(max_length=40, verbose_name='College Name')),
                ('roll', models.CharField(max_length=5, verbose_name='Roll')),
                ('dateTime', models.DateTimeField(verbose_name='DateTime')),
            ],
        ),
    ]
