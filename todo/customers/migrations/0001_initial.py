# Generated by Django 3.1.3 on 2021-07-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tc_no', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('town', models.CharField(max_length=120)),
            ],
        ),
    ]