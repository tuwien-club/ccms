# Generated by Django 2.2 on 2020-10-27 21:46

import django.db.models.deletion
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("wagtailcore", "0052_pagelogentry")]

    operations = [
        migrations.CreateModel(
            name="LicenseSnippet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                ("description", models.TextField(blank=True)),
                ("version", models.TextField(blank=True)),
                ("url", models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="SystemMessagesSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title_404",
                    models.CharField(
                        default="Page not found", max_length=255, verbose_name="Title"
                    ),
                ),
                (
                    "body_404",
                    wagtail.core.fields.RichTextField(
                        default="<p>You may be trying to find a page that doesn&rsquo;t exist or has been moved.</p>",
                        verbose_name="Text",
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.Site",
                    ),
                ),
            ],
            options={"verbose_name": "system messages"},
        ),
        migrations.CreateModel(
            name="SocialMediaSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "twitter_handle",
                    models.CharField(
                        blank=True,
                        help_text="Your Twitter username without the @, e.g. katyperry",
                        max_length=255,
                    ),
                ),
                (
                    "facebook_app_id",
                    models.CharField(
                        blank=True, help_text="Your Facebook app ID.", max_length=255
                    ),
                ),
                (
                    "default_sharing_text",
                    models.CharField(
                        blank=True,
                        help_text="Default sharing text to use if social text has not been set on a page.",
                        max_length=255,
                    ),
                ),
                (
                    "site_name",
                    models.CharField(
                        blank=True,
                        default="esite",
                        help_text="Site name, used by Open Graph.",
                        max_length=255,
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.Site",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Button",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("button_title", models.CharField(max_length=255, null=True)),
                (
                    "button_embed",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("button_link", models.URLField(blank=True, null=True)),
                (
                    "button_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.Page",
                    ),
                ),
            ],
        ),
    ]
