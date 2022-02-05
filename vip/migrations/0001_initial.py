# Generated by Django 3.2 on 2022-02-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_size', models.CharField(choices=[('4-5', '4-6'), ('6-8', '6-8'), (' ', ' ')], default=' ', max_length=3)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]