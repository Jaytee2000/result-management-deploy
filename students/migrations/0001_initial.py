# Generated by Django 5.0.2 on 2024-02-18 21:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("student_classes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("student_name", models.CharField(max_length=100)),
                ("student_roll", models.IntegerField(unique=True)),
                ("student_email", models.EmailField(max_length=254)),
                (
                    "student_gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        max_length=8,
                    ),
                ),
                (
                    "student_date_of_birth",
                    models.DateField(default=datetime.date(2024, 2, 18)),
                ),
                ("student_reg", models.DateField(auto_now_add=True)),
                (
                    "student_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_classes.studentclass",
                    ),
                ),
            ],
        ),
    ]
