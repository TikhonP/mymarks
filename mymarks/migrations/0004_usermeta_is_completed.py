# Generated by Django 3.0.2 on 2020-02-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymarks', '0003_auto_20200215_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermeta',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
