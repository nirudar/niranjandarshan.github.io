# Generated by Django 4.0.6 on 2024-03-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='job_end_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='experience',
            name='job_responsibility',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='experience',
            name='job_start_date',
            field=models.CharField(max_length=10),
        ),
    ]
