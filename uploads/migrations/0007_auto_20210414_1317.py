# Generated by Django 3.0.14 on 2021-04-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_auto_20210414_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='task',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='task_id',
            field=models.CharField(default=1111, max_length=255),
            preserve_default=False,
        ),
    ]
