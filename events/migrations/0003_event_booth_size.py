# Generated by Django 3.2 on 2022-02-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='booth_size',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
