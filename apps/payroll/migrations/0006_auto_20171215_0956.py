# Generated by Django 2.0 on 2017-12-15 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0005_auto_20171215_0948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='present_days',
            new_name='total_present_days',
        ),
    ]
