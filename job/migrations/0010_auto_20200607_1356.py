# Generated by Django 3.0.7 on 2020-06-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20200606_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='college',
            field=models.CharField(default='w', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='subject',
            field=models.CharField(max_length=35),
        ),
    ]
