# Generated by Django 2.2 on 2020-10-27 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0052_pagelogentry"),
        ("images", "0001_initial"),
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="featured_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.SNEKImage",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="hero_button_link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.Page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="listing_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose the image you wish to be displayed when this page appears in listings",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.SNEKImage",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="news_link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.Page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="pages_link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.Page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="social_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.SNEKImage",
            ),
        ),
    ]