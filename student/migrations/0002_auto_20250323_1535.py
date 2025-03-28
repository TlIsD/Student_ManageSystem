# Generated by Django 3.2 on 2025-03-23 15:35

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(default='/avatar/default.jpg', upload_to=student.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='stu',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
