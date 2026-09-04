from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Beneficiary",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("place_of_birth", models.CharField(max_length=120)),
                ("gender", models.CharField(default="Female", max_length=20)),
                ("nationality", models.CharField(max_length=40)),
                ("marital_status", models.CharField(max_length=20)),
                ("settlement_camp", models.CharField(max_length=100)),
                ("registration_date", models.DateField()),
                ("date_of_joining", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
