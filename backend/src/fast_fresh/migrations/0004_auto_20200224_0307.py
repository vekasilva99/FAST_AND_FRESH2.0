# Generated by Django 3.0.3 on 2020-02-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_fresh', '0003_iva_iva_porcentaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type_of_product',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]
