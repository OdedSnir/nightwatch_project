# Generated by Django 4.2.15 on 2024-08-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="personal_number",
            field=models.CharField(default="NoNumber", max_length=20, unique=True),
        ),
    ]
