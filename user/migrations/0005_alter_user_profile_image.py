# Generated by Django 4.2.1 on 2023-05-26 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_user_phone_number_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]