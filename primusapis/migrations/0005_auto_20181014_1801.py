# Generated by Django 2.1.2 on 2018-10-14 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primusapis', '0004_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('U', 'unknown'), ('S', 'safe')], default='U', max_length=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_of',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
