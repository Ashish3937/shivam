# Generated by Django 2.1 on 2019-02-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0003_booking_additional_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='landmark',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]