# Generated by Django 4.2.4 on 2023-08-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsl_server', '0002_alter_servicealert_entityid'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicealert',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
