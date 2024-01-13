# Generated by Django 5.0.1 on 2024-01-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='karbar',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='karbar',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='karbar',
            name='groups',
            field=models.ManyToManyField(related_name='karbar_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='karbar',
            name='user_permissions',
            field=models.ManyToManyField(related_name='karbar_permissions', to='auth.permission'),
        ),
    ]
