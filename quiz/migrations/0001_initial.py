# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprehension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('comprehension_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('question_text', models.TextField()),
                ('question_comprehension', models.ForeignKey(to='quiz.Comprehension')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('submission_created', models.DateTimeField(auto_now_add=True)),
                ('submission_submitted', models.DateTimeField(auto_now=True)),
                ('submission_choice', models.CharField(max_length=255, choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D'), ('X', 'Not Submitted')])),
                ('submission_question', models.ForeignKey(to='quiz.Question')),
            ],
        ),
    ]
