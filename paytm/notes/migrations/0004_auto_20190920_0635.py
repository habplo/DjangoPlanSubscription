# Generated by Django 2.2 on 2019-09-20 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20190916_0629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'permissions': (('add_only_10_notes', 'To provide 10 notes facility'), ('add_only_5_task', 'To provide 5 task facility'), ('add_only_20_notes', 'To provide 20 notes facility'), ('add_only_10_task', 'To provide 10 task facility'))},
        ),
    ]
