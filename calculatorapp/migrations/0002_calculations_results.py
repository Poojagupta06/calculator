# Generated by Django 3.1.2 on 2020-10-21 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculatorapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculations',
            name='results',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
