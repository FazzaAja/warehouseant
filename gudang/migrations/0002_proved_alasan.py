# Generated by Django 4.1.5 on 2023-01-14 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gudang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proved',
            name='alasan',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]