# Generated by Django 4.2.4 on 2023-08-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsl_server', '0003_servicealert_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicealert',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
