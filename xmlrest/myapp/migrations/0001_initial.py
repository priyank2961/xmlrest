# Generated by Django 4.1.5 on 2023-01-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]
