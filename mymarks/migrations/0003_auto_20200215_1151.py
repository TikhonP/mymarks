# Generated by Django 3.0.2 on 2020-02-15 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('mymarks', '0002_auto_20200112_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('math', models.IntegerField(default=-1)),
                ('russian', models.IntegerField(default=-1)),
                ('chemistry', models.IntegerField(default=-1)),
            ],
        ),
        migrations.AlterField(
            model_name='mark',
            name='value',
            field=models.CharField(max_length=2),
        ),
    ]
