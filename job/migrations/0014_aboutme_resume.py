# Generated by Django 3.0.7 on 2020-06-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_auto_20200608_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='resume',
            field=models.FileField(default='dsf', upload_to='media/resume'),
            preserve_default=False,
        ),
    ]
