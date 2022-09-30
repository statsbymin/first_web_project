# Generated by Django 4.0.7 on 2022-09-28 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ('-upload_dt',)},
        ),
        migrations.AddField(
            model_name='photo',
            name='project_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Project_Name'),
        ),
    ]
