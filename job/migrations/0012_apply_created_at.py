# Generated by Django 3.1.7 on 2021-03-02 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
