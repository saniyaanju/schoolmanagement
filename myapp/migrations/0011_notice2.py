# Generated by Django 5.0.1 on 2024-02-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField(blank=True, default=0, null=True)),
            ],
        ),
    ]