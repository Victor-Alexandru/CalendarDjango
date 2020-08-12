# Generated by Django 2.2 on 2020-08-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('made_sport', models.BooleanField(default=False)),
                ('made_reading', models.BooleanField(default=False)),
                ('made_health_eating', models.BooleanField(default=False)),
                ('made_r', models.BooleanField(default=False)),
                ('made_pos_afir', models.BooleanField(default=False)),
            ],
        ),
    ]
