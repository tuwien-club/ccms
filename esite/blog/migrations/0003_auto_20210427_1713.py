# Generated by Django 3.1.8 on 2021-04-27 15:13

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail_headless_preview.models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtaildocs", "0010_document_file_hash"),
        ("wagtailcore", "0059_apply_collection_ordering"),
        ("wagtailimages", "0022_uploadedimage"),
        ("wagtailmedia", "0003_copy_media_permissions_to_collections"),
        ("images", "0002_auto_20201027_2246"),
        ("home", "0002_auto_20201027_2246"),
    ]

    operations = [
        migrations.CreateModel(
            name="Advert",
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
                ("url", models.URLField(blank=True, null=True)),
                ("text", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="AuthorPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("social_text", models.CharField(blank=True, max_length=255)),
                (
                    "listing_title",
                    models.CharField(
                        blank=True,
                        help_text="Override the page title used when this page appears in listings",
                        max_length=255,
                    ),
                ),
                (
                    "listing_summary",
                    models.CharField(
                        blank=True,
                        help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Search description' field above is not defined.",
                        max_length=255,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "listing_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Choose the image you wish to be displayed when this page appears in listings",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.snekimage",
                    ),
                ),
                (
                    "social_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.snekimage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="BlogPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("social_text", models.CharField(blank=True, max_length=255)),
                (
                    "listing_title",
                    models.CharField(
                        blank=True,
                        help_text="Override the page title used when this page appears in listings",
                        max_length=255,
                    ),
                ),
                (
                    "listing_summary",
                    models.CharField(
                        blank=True,
                        help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Search description' field above is not defined.",
                        max_length=255,
                    ),
                ),
                ("date", models.DateField(verbose_name="Post date")),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.core.blocks.CharBlock(
                                    form_classname="full title"
                                ),
                            ),
                            ("paragraph", wagtail.core.blocks.RichTextBlock()),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                            ("decimal", wagtail.core.blocks.DecimalBlock()),
                            ("date", wagtail.core.blocks.DateBlock()),
                            ("datetime", wagtail.core.blocks.DateTimeBlock()),
                            (
                                "gallery",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.core.blocks.CharBlock(
                                                form_classname="full title"
                                            ),
                                        ),
                                        (
                                            "images",
                                            wagtail.core.blocks.StreamBlock(
                                                [
                                                    (
                                                        "image",
                                                        wagtail.core.blocks.StructBlock(
                                                            [
                                                                (
                                                                    "caption",
                                                                    wagtail.core.blocks.CharBlock(
                                                                        form_classname="full title"
                                                                    ),
                                                                ),
                                                                (
                                                                    "image",
                                                                    wagtail.images.blocks.ImageChooserBlock(),
                                                                ),
                                                            ]
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "video",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "youtube_link",
                                            wagtail.embeds.blocks.EmbedBlock(
                                                required=False
                                            ),
                                        )
                                    ]
                                ),
                            ),
                            (
                                "objectives",
                                wagtail.core.blocks.ListBlock(
                                    wagtail.core.blocks.CharBlock()
                                ),
                            ),
                        ]
                    ),
                ),
                (
                    "advert",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="home.advert",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="home.authorpage",
                    ),
                ),
                (
                    "book_file",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtaildocs.document",
                    ),
                ),
                (
                    "cover",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "featured_media",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailmedia.media",
                    ),
                ),
                (
                    "listing_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Choose the image you wish to be displayed when this page appears in listings",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.snekimage",
                    ),
                ),
                (
                    "social_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.snekimage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail_headless_preview.models.HeadlessPreviewMixin,
                "wagtailcore.page",
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=255)),
                ("job", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="articles_link",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="articles_linktext",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="articles_title",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="featured_image",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="featured_pages_title",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="hero_button_link",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="hero_button_text",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="hero_introduction",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="hero_title",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="listing_image",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="listing_summary",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="listing_title",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="news_link",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="news_linktext",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="news_title",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="pages_link",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="pages_linktext",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="social_image",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="social_text",
        ),
        migrations.CreateModel(
            name="BlogPageRelatedLink",
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
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField()),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_links",
                        to="home.blogpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Author",
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
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("role", models.CharField(max_length=255)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="authors",
                        to="home.blogpage",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="home.person",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
