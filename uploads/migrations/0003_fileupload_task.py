# Generated by Django 3.0.14 on 2021-04-14 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0008_chordcounter'),
        ('uploads', '0002_auto_20200102_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_results.TaskResult'),
        ),
    ]
