# Generated by Django 2.0.1 on 2018-01-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelerinage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_pel', models.DateField()),
                ('frais', models.IntegerField(null=True)),
            ],
        ),
    ]
