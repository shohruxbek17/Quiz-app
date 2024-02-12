# Generated by Django 5.0.1 on 2024-02-08 20:59

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0011_alter_test_category_alter_test_end_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='category',
        ),
        migrations.RemoveField(
            model_name='checkanswer',
            name='student',
        ),
        migrations.RemoveField(
            model_name='checkanswer',
            name='test',
        ),
        migrations.RemoveField(
            model_name='checkquestion',
            name='checktest',
        ),
        migrations.RemoveField(
            model_name='checkquestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='test',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.RemoveField(
            model_name='question',
            name='a',
        ),
        migrations.RemoveField(
            model_name='question',
            name='b',
        ),
        migrations.RemoveField(
            model_name='question',
            name='c',
        ),
        migrations.RemoveField(
            model_name='question',
            name='d',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='true_answer',
        ),
        migrations.AddField(
            model_name='question',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='question',
            name='html',
            field=models.TextField(default=1, verbose_name='Question Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Has been published?'),
        ),
        migrations.AddField(
            model_name='question',
            name='maximum_marks',
            field=models.DecimalField(decimal_places=2, default=4, max_digits=6, verbose_name='Maximum Marks'),
        ),
        migrations.AddField(
            model_name='question',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is this answer correct?')),
                ('html', models.TextField(verbose_name='Choice Text')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='test_app.question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuizProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('total_score', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total Score')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttemptedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Was this attempt correct?')),
                ('marks_obtained', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Marks Obtained')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.question')),
                ('selected_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.choice')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='attempts', to= 'test_app.Profile'))
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='CheckAnswer',
        ),
        migrations.DeleteModel(
            name='Checkquestion',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
