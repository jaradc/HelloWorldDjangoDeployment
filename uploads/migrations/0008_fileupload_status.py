# Generated by Django 3.0.14 on 2021-04-14 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0007_auto_20210414_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='status',
            field=models.CharField(default='SUCCESS', max_length=20),
            preserve_default=False,
        ),
    ]
