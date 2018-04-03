# Generated by Django 2.0.3 on 2018-04-03 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('login', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('cpf', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('doctorName', models.CharField(max_length=255)),
                ('birth', models.DateField()),
                ('ddd', models.IntegerField()),
                ('whatsapp', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('howDidYouKnow', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('profile', models.CharField(max_length=255)),
                ('wantOngs', models.BooleanField(default=False)),
                ('promoted', models.BooleanField(default=False)),
                ('voluntaryHours', models.IntegerField()),
                ('created', models.DateField()),
                ('observation', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProfileFeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
