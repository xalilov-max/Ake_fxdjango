# Generated by Django 5.2 on 2025-05-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_aboutpage_statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Yangilik sarlavhasi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/', verbose_name='Rasm')),
                ('short_text', models.TextField(verbose_name='Qisqa matn')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Yangilik',
                'verbose_name_plural': 'Yangiliklar',
                'ordering': ['-created_at'],
            },
        ),
    ]
