# Generated by Django 5.1.6 on 2025-03-30 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseResults',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('case_name', models.CharField(max_length=255)),
                ('verdict', models.TextField()),
                ('judgment_date', models.DateField()),
                ('qadi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.qadi')),
            ],
        ),
    ]
