# Generated by Django 5.1 on 2024-08-27 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_aboutsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('about_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.aboutsection')),
            ],
        ),
    ]
