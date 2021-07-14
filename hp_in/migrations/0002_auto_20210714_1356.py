# Generated by Django 3.0.7 on 2021-07-14 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_in', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='Generosity',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='information',
            name='Healthy_life_expectancy',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='information',
            name='Ladder_score',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='information',
            name='Logged_GDP_per_capita',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
