# Generated by Django 4.1.4 on 2023-05-08 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                (
                    "create_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "text",
                    models.TextField(max_length=2000, verbose_name="Текст отзыва"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_comments",
                        to="app_product.product",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "комментарий",
                "verbose_name_plural": "комментарии",
                "db_table": "comments",
                "ordering": ["-create_at"],
            },
        ),
    ]
