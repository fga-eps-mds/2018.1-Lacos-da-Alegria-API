# Generated by Django 2.0.4 on 2018-04-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('volunteers', models.IntegerField()),
                ('limit', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
                ('subscription', models.BooleanField(default=False)),
                ('call', models.BooleanField(default=False)),
            ],
        ),
    ]
