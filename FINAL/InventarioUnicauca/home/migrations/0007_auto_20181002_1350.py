# Generated by Django 2.0.6 on 2018-10-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20181002_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='codigo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=100),
        ),
    ]