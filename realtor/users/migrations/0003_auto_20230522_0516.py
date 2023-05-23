# Generated by Django 3.2.18 on 2023-05-22 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20230522_0508"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="agent",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="users.agent"),
        ),
        migrations.AlterField(
            model_name="application",
            name="user",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
