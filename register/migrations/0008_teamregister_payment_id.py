# Generated by Django 4.1.7 on 2023-04-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0007_teamregister_paid"),
    ]

    operations = [
        migrations.AddField(
            model_name="teamregister",
            name="payment_id",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
