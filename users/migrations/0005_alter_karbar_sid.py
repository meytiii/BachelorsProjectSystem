# Generated by Django 5.0.1 on 2024-01-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_karbar_sid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karbar',
            name='sid',
            field=models.CharField(default='1000000000', max_length=10, unique=True, verbose_name='Student/Professor ID'),
        ),
    ]
