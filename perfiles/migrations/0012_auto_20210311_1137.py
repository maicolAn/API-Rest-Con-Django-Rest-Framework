# Generated by Django 3.1.6 on 2021-03-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0011_auto_20201222_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hipertension',
            name='imc',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
