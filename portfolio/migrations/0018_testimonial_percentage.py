# Generated by Django 5.1 on 2024-09-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_alter_testimonial_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='percentage',
            field=models.IntegerField(default=100, help_text="'.5 => 8', '1 => 15', '1.5 => 28', '2 => 35', '2.5 => 48', '3 => 55', '3.5 => 68', '4 => 80', '4.5 => 88', '5 => 100'"),
        ),
    ]
