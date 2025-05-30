# Generated by Django 5.2 on 2025-05-07 22:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kategoriya nomi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Daraja nomi')),
            ],
            options={
                'verbose_name': 'Daraja',
                'verbose_name_plural': 'Darajalar',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category', verbose_name='Kategoriya'),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.level', verbose_name='Daraja'),
        ),
    ]
