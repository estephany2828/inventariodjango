# Generated by Django 2.0.6 on 2018-10-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181002_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip',
            name='ip_numero',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='ip',
            name='mascara',
            field=models.GenericIPAddressField(null=True),
        ),
    ]