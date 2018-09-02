# Generated by Django 2.1 on 2018-09-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_tracking', '0006_auto_20180401_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apirequestlog',
            name='method',
            field=models.CharField(db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='apirequestlog',
            name='status_code',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
