# Generated by Django 4.1.3 on 2022-12-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_headings_btncode_alter_headings_subheading'),
    ]

    operations = [
        migrations.AddField(
            model_name='headings',
            name='icon',
            field=models.CharField(default='', max_length=150),
        ),
    ]
