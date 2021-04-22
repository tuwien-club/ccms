from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_group(name, permissions=[]):
    from django.contrib.auth.models import Group

    group, created = Group.objects.get_or_create(name=name)
    [group.permissions.add(permission) for permission in permissions]


def create_user(username, password, groups=[], **kwargs):
    from django.contrib.auth import get_user_model
    from django.contrib.auth.models import Group

    User = get_user_model()

    user = User.objects.create(username=username, **kwargs)
    user.set_password(password)
    user.save()

    [user.groups.add(Group.objects.get(name=group)) for group in groups]


def define_groups(sender, **kwargs):
    create_group("system")


def define_users(sender, **kwargs):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    if not User.objects.exists():
        create_user(
            username="admin",
            password="ciscocisco",
            is_superuser=True,
            groups=["system"],
        )
        create_user(username="cisco", password="ciscocisco", groups=["system"])


class UsersConfig(AppConfig):
    name = "esite.user"

    def ready(self):
        post_migrate.connect(define_groups, sender=self)
        post_migrate.connect(define_users, sender=self)

        # if you have other signals e.g. post_save, you can include it
        # like the one below.
        # from .signals import (create_site_profile)


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2021 Nico Schett
