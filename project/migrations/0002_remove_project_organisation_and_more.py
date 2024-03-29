# Generated by Django 4.0.6 on 2024-03-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='organisation',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_start_date',
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.FileField(default=None, max_length=300, null=True, upload_to='project_image/'),
        ),
    ]
