import django.contrib.auth.validators
from bifrost.api.models import GraphQLBoolean, GraphqlDatetime, GraphQLString
from django.contrib.auth.models import AbstractUser
from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


# Extend AbstractUser Model from django.contrib.auth.models
class SNEKUser(AbstractUser, ClusterableModel):
    username = models.CharField(
        "username",
        null=True,
        blank=False,
        error_messages={"unique": "A user with that username already exists."},
        help_text="Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.",
        max_length=36,
        unique=True,
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
    )
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=False
    )
    telephone = models.CharField(null=False, blank=False, max_length=40)
    address = models.CharField(null=True, blank=True, max_length=60)
    city = models.CharField(null=True, blank=True, max_length=60)
    postal_code = models.CharField(null=True, blank=True, max_length=12)
    country = models.CharField(null=True, blank=True, max_length=2)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("username"),
                FieldPanel("first_name"),
                FieldPanel("last_name"),
                FieldPanel("email"),
                FieldPanel("birthdate"),
                FieldPanel("telephone"),
                FieldPanel("address"),
                FieldPanel("city"),
                FieldPanel("postal_code"),
                FieldPanel("country"),
            ],
            "Details",
        ),
        MultiFieldPanel(
            [
                FieldPanel("is_active"),
            ],
            "Settings",
        ),
    ]

    graphql_fields = [
        GraphQLString("username"),
        GraphQLString("first_name"),
        GraphQLString("last_name"),
        GraphQLString("email"),
        GraphqlDatetime("birthdate"),
        GraphQLString("telephone"),
        GraphQLString("address"),
        GraphQLString("city"),
        GraphQLString("postal_code"),
        GraphQLString("country"),
        GraphQLBoolean("is_active"),
    ]

    # Custom save function
    def save(self, *args, **kwargs):
        super(SNEKUser, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}"


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2021 Nico Schett
