# Generated by Django 3.0.14 on 2021-04-14 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0008_chordcounter'),
        ('uploads', '0005_auto_20210414_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='django_celery_results.TaskResult'),
        ),
    ]
