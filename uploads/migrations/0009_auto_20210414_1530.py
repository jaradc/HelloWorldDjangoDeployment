# Generated by Django 3.0.14 on 2021-04-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0008_fileupload_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='status',
            field=models.CharField(default='CHECKING', max_length=20),
        ),
    ]
