# Generated by Django 5.1.6 on 2025-03-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_letterroutine_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterroutine',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
