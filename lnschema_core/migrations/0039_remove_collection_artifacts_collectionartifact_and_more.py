# Generated by Django 5.1 on 2024-01-07 19:08

import django.db.models.deletion
from django.db import migrations, models

import lnschema_core.models


class Migration(migrations.Migration):
    dependencies = [
        ("lnschema_core", "0038_alter_collection_artifact_alter_collection_artifacts_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CollectionArtifact",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("collection", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="lnschema_core.collection")),
                ("artifact", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="lnschema_core.artifact")),
            ],
            options={
                "unique_together": {("collection", "artifact")},
            },
            bases=(models.Model, lnschema_core.models.LinkORM),
        ),
        migrations.AddField(
            model_name="collection",
            name="unordered_artifacts",
            field=models.ManyToManyField(related_name="collections", through="lnschema_core.CollectionArtifact", to="lnschema_core.artifact"),
        ),
        migrations.RunSQL(
            "INSERT INTO lnschema_core_collectionartifact (id, collection_id, artifact_id) SELECT id, collection_id, artifact_id FROM lnschema_core_collection_artifacts"
        ),
        migrations.RemoveField(
            model_name="collection",
            name="artifacts",
        ),
    ]
