from bifrost.models import GraphQLBoolean, GraphQLSnippet, GraphQLString
from django.db import models
from wagtail.images.models import AbstractImage, AbstractRendition, Image


# We define our own custom image class to replace wagtailimages.Image,
# providing various additional data fields
class SNEKImage(AbstractImage):
    license = models.ForeignKey(
        "utils.LicenseSnippet",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    description = models.TextField(blank=True, max_length=165)
    author = models.CharField(blank=True, max_length=165, null=True)
    image_source_url = models.URLField(blank=True)

    admin_form_fields = Image.admin_form_fields + (
        "description",
        "author",
        "license",
        "image_source_url",
    )

    graphql_fields = [
        GraphQLSnippet("license", snippet_model="utils.Button"),
        GraphQLString("description"),
        GraphQLString("author"),
        GraphQLBoolean("image_source_url"),
    ]


class SNEKPersonAvatarImage(AbstractImage):
    pass


class SNEKAchievementImage(AbstractImage):
    pass


class Rendition(AbstractRendition):
    image = models.ForeignKey(
        "SNEKImage", related_name="renditions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
