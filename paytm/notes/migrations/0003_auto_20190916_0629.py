# Generated by Django 2.2 on 2019-09-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20190913_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
