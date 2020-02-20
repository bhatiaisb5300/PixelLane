# Generated by Django 2.1.7 on 2020-02-10 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='abstract/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='architechture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='architechture/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='bird',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='bird/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='exif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('shutterspeed', models.CharField(max_length=50)),
                ('focallength', models.CharField(max_length=50)),
                ('aperture', models.CharField(max_length=50)),
                ('iso', models.CharField(max_length=50)),
                ('lens', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='landscape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='wildlife/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='lifestyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='lifestyle/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='long_exposure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='long_exposure/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='night_life',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='night_life/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='portraiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='portrait/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='street/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='vogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='vogue/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='wildlife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=20)),
                ('shot_on', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='wildlife/images')),
                ('description', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('batch', models.CharField(max_length=4)),
                ('insta', models.URLField()),
            ],
        ),
    ]
