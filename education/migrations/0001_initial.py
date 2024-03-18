# Generated by Django 4.0.6 on 2023-11-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.TextField(max_length=100)),
                ('university', models.TextField(max_length=250)),
                ('college_address', models.TextField(max_length=250)),
                ('course_start_date', models.PositiveIntegerField(max_length=4)),
                ('course_end_date', models.PositiveIntegerField(max_length=4)),
                ('course_description', models.TextField(max_length=100)),
            ],
        ),
    ]