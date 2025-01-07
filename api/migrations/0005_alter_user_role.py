# Generated by Django 5.1.4 on 2025-01-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('developer', 'Developer'), ('user', 'User')], default='user', max_length=20),
        ),
    ]
