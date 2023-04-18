# Generated by Django 3.2.18 on 2023-04-06 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.CharField(blank=True, default="", max_length=50)),
                ("price", models.IntegerField()),
                ("city", models.CharField(max_length=5)),
                ("district", models.CharField(max_length=3)),
                ("zone", models.CharField(max_length=3)),
                (
                    "property_type",
                    models.IntegerField(choices=[(1, "Purchase"), (2, "Longterm"), (3, "Monthly")], default=1),
                ),
                (
                    "detailed_type",
                    models.IntegerField(
                        choices=[(1, "One Room"), (2, "Two Room"), (3, "Officetel"), (4, "Apartment")], default=4
                    ),
                ),
                ("size", models.IntegerField()),
                ("description", models.TextField()),
                ("maintenance_cost", models.IntegerField()),
                (
                    "status",
                    models.IntegerField(choices=[(1, "Available"), (2, "In Progress"), (3, "Done")], default=1),
                ),
            ],
        ),
    ]
