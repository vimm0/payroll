# Generated by Django 2.0 on 2017-12-15 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=255)),
                ('present_days', models.IntegerField(default=0)),
                ('total_days', models.IntegerField(default=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_days', models.PositiveIntegerField()),
                ('salary', models.PositiveIntegerField(default=0)),
                ('payment', models.PositiveIntegerField(default=0, editable=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll.Employee'),
        ),
    ]
