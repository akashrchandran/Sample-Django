# Generated by Django 5.0.4 on 2024-06-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_file_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="file_size",
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]