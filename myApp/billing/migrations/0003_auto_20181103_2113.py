# Generated by Django 2.1 on 2018-11-03 19:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20181103_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingprofile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]