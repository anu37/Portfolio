# Generated by Django 3.0.7 on 2020-06-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20200606_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('link', models.URLField()),
                ('image_path', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
