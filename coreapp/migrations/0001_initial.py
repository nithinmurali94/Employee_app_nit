# Generated by Django 3.2.6 on 2021-08-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_code', models.CharField(max_length=250)),
                ('employee_name', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
