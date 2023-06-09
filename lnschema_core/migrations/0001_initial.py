# Generated by Django 4.2.1 on 2023-06-09 11:43

from typing import List

import django.db.models.deletion
from django.db import migrations, models

import lnschema_core.ids
import lnschema_core.types
import lnschema_core.users


class Migration(migrations.Migration):
    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                ("id", models.CharField(max_length=20, primary_key=True, serialize=False)),
                ("name", models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ("suffix", models.CharField(db_index=True, default=None, max_length=30, null=True)),
                ("size", models.BigIntegerField(db_index=True, null=True)),
                ("hash", models.CharField(db_index=True, default=None, max_length=86, null=True)),
                ("key", models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Folder",
            fields=[
                ("id", models.CharField(default=lnschema_core.ids.folder, max_length=20, primary_key=True, serialize=False)),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("key", models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Run",
            fields=[
                ("id", models.CharField(default=lnschema_core.ids.run, max_length=20, primary_key=True, serialize=False)),
                ("name", models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ("external_id", models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("run_at", models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.CharField(default=None, max_length=8, primary_key=True, serialize=False)),
                ("handle", models.CharField(db_index=True, default=None, max_length=30, unique=True)),
                ("email", models.CharField(db_index=True, default=None, max_length=255, unique=True)),
                ("name", models.CharField(db_index=True, max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Transform",
            fields=[
                ("id", models.CharField(db_index=True, default=None, max_length=14, primary_key=True, serialize=False)),
                ("name", models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ("short_name", models.CharField(db_index=True, default=None, max_length=30, null=True)),
                ("stem_id", models.CharField(db_index=True, default=lnschema_core.ids.transform, max_length=12)),
                ("version", models.CharField(db_index=True, default="0", max_length=10)),
                (
                    "type",
                    models.CharField(
                        choices=[("pipeline", "pipeline"), ("notebook", "notebook"), ("app", "app"), ("api", "api")],
                        db_index=True,
                        default=lnschema_core.types.TransformType["pipeline"],
                        max_length=20,
                    ),
                ),
                ("reference", models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id, on_delete=django.db.models.deletion.PROTECT, related_name="created_transforms", to="lnschema_core.user"
                    ),
                ),
            ],
            options={
                "managed": True,
                "unique_together": {("stem_id", "version")},
            },
        ),
        migrations.CreateModel(
            name="Storage",
            fields=[
                ("id", models.CharField(db_index=True, default=lnschema_core.ids.storage, max_length=8, primary_key=True, serialize=False)),
                ("root", models.CharField(db_index=True, default=None, max_length=255)),
                ("type", models.CharField(db_index=True, max_length=30)),
                ("region", models.CharField(db_index=True, default=None, max_length=63, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id, on_delete=django.db.models.deletion.PROTECT, related_name="created_storages", to="lnschema_core.user"
                    ),
                ),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="RunInput",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="lnschema_core.file")),
                ("run", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="lnschema_core.run")),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="run",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id, on_delete=django.db.models.deletion.PROTECT, related_name="created_runs", to="lnschema_core.user"
            ),
        ),
        migrations.AddField(
            model_name="run",
            name="inputs",
            field=models.ManyToManyField(related_name="input_of", through="lnschema_core.RunInput", to="lnschema_core.file"),
        ),
        migrations.AddField(
            model_name="run",
            name="transform",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="runs", to="lnschema_core.transform"),
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.CharField(default=lnschema_core.ids.project, max_length=8, primary_key=True, serialize=False)),
                ("name", models.CharField(db_index=True, default=None, max_length=255, unique=True)),
                ("external_id", models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id, on_delete=django.db.models.deletion.PROTECT, related_name="created_projects", to="lnschema_core.user"
                    ),
                ),
                ("files", models.ManyToManyField(related_name="projects", to="lnschema_core.file")),
                ("folders", models.ManyToManyField(related_name="projects", to="lnschema_core.folder")),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="folder",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id, on_delete=django.db.models.deletion.PROTECT, related_name="created_folders", to="lnschema_core.user"
            ),
        ),
        migrations.AddField(
            model_name="folder",
            name="files",
            field=models.ManyToManyField(related_name="folders", to="lnschema_core.file"),
        ),
        migrations.AddField(
            model_name="folder",
            name="storage",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name="folders", to="lnschema_core.storage"),
        ),
        migrations.AddField(
            model_name="file",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id, on_delete=django.db.models.deletion.PROTECT, related_name="created_files", to="lnschema_core.user"
            ),
        ),
        migrations.AddField(
            model_name="file",
            name="run",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name="outputs", to="lnschema_core.run"),
        ),
        migrations.AddField(
            model_name="file",
            name="storage",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="files", to="lnschema_core.storage"),
        ),
        migrations.AddField(
            model_name="file",
            name="transform",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name="files", to="lnschema_core.transform"),
        ),
        migrations.CreateModel(
            name="Featureset",
            fields=[
                ("id", models.CharField(default=None, max_length=64, primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_featuresets",
                        to="lnschema_core.user",
                    ),
                ),
                ("files", models.ManyToManyField(related_name="featuresets", to="lnschema_core.file")),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.AlterUniqueTogether(
            name="folder",
            unique_together={("storage", "key")},
        ),
        migrations.AlterUniqueTogether(
            name="file",
            unique_together={("storage", "key")},
        ),
    ]
