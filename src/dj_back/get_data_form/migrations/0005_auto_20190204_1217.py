# Generated by Django 2.1.5 on 2019-02-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data_form', '0004_result_result_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result_file',
            field=models.FilePathField(),
        ),
    ]
