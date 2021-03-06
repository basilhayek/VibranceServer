# Generated by Django 2.2.2 on 2019-07-26 18:54

from django.db import migrations, models
import medication.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=300)),
                ('frequency', models.CharField(max_length=200)),
                ('refillDate', models.CharField(max_length=100)),
                ('adherence', medication.models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
