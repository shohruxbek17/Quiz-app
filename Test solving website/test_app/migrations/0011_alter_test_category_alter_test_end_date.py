# Generated by Django 5.0.1 on 2024-02-08 18:50

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0010_alter_test_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='category',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.category'),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 18, 18, 50, 1, 465881, tzinfo=datetime.timezone.utc)),
        ),
    ]
