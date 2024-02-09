# Generated by Django 5.0.1 on 2024-02-08 18:19

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_rename_find_question_checkanswer_finded_question_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='true_ans',
            new_name='true_answer',
        ),
        migrations.AddField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 18, 18, 19, 7, 992444, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='test',
            name='maximum_attemps',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='test',
            name='pass_percentage',
            field=models.PositiveBigIntegerField(default=60),
        ),
        migrations.AddField(
            model_name='test',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='test',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='test_app.category'),
        ),
    ]