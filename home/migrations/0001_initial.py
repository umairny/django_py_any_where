# Generated by Django 4.1.3 on 2022-12-08 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Headings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('subHeading', models.CharField(max_length=500)),
                ('icon', models.CharField(default='', max_length=150)),
                ('btnApp', models.CharField(max_length=50)),
                ('btnCode', models.CharField(max_length=200)),
                ('videoLink', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_feature', models.CharField(max_length=500)),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.features')),
            ],
        ),
        migrations.AddField(
            model_name='features',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.headings'),
        ),
    ]
