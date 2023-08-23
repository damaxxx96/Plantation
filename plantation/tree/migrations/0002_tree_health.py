# Generated by Django 4.2.2 on 2023-08-14 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tree", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tree",
            name="health",
            field=models.CharField(
                choices=[("good", "Good"), ("average", "Average"), ("poor", "Poor")],
                default="average",
                max_length=10,
            ),
        ),
    ]
