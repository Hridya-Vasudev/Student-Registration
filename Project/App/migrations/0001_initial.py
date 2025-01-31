# Generated by Django 5.0.6 on 2024-07-04 11:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_no', models.CharField(max_length=20)),
                ('enquiry_date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact_no', models.CharField(max_length=20)),
                ('whatsapp_no', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('has_work_experience', models.BooleanField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.college')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.student')),
            ],
        ),
    ]
