# Generated by Django 5.1.4 on 2025-01-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.FloatField(null=True),
        ),
    ]
