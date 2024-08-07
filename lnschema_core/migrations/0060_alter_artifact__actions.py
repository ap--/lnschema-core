# Generated by Django 5.2 on 2024-08-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "lnschema_core",
            "0059_alter_artifact__accessor_alter_artifact__hash_type_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="artifact",
            name="_actions",
            field=models.ManyToManyField(
                related_name="_action_targets", to="lnschema_core.artifact"
            ),
        ),
    ]
