# Generated by Django 4.2.15 on 2024-09-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="available",
            field=models.BooleanField(default=True),
        ),
    ]
