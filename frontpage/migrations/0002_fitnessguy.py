# Generated by Django 2.0.6 on 2018-06-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fitnessguy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField()),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
            ],
        ),
    ]