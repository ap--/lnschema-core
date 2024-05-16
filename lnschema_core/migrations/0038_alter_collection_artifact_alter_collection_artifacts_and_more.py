# Generated by Django 4.2.5 on 2023-12-23 23:10

import django.db.models.deletion
from django.db import migrations, models

import lnschema_core.users


class Migration(migrations.Migration):
    dependencies = [("lnschema_core", "0037_rename_dataset_to_collection")]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="artifact",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="collection",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="artifacts",
            field=models.ManyToManyField(
                related_name="collections", to="lnschema_core.artifact"
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_collections",
                to="lnschema_core.user",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="feature_sets",
            field=models.ManyToManyField(
                related_name="collections",
                through="lnschema_core.CollectionFeatureSet",
                to="lnschema_core.featureset",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="input_of",
            field=models.ManyToManyField(
                related_name="input_collections", to="lnschema_core.run"
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="run",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="output_collections",
                to="lnschema_core.run",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="transform",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="output_collections",
                to="lnschema_core.transform",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="ulabels",
            field=models.ManyToManyField(
                related_name="collections",
                through="lnschema_core.CollectionULabel",
                to="lnschema_core.ulabel",
            ),
        ),
    ]
