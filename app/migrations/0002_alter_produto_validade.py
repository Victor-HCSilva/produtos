# Generated by Django 5.1.4 on 2025-01-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='validade',
            field=models.DateField(blank=True, null=True),
        ),
    ]