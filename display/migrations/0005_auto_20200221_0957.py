# Generated by Django 2.1.7 on 2020-02-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_auto_20200221_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
