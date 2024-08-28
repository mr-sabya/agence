# Generated by Django 5.1 on 2024-08-28 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio_technologies_delete_portfoliotechnology'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(help_text='2018-2022', max_length=15)),
                ('designation', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=255)),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.teammember')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(max_length=100)),
                ('year', models.CharField(help_text='2018-2022', max_length=15)),
                ('school', models.CharField(max_length=255)),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.teammember')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('progress', models.IntegerField()),
                ('team_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.teammember')),
            ],
        ),
    ]
