# Generated by Django 5.1 on 2024-08-27 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_aboutsection_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_heading', models.CharField(max_length=15)),
                ('highlight_heading', models.CharField(max_length=15)),
                ('heading', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Goal Section',
                'verbose_name_plural': 'Goal Section',
            },
        ),
        migrations.CreateModel(
            name='GoalCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('text', models.CharField(max_length=100)),
                ('goal_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.goalsection')),
            ],
        ),
    ]
