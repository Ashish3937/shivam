# Generated by Django 2.1.7 on 2019-04-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0008_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customer_phone',
            field=models.IntegerField(),
        ),
    ]