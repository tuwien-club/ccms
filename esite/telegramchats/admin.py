# Register your models here.
from django.db.models import Q
from django.contrib.admin import SimpleListFilter
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from .models import (
    TelegramChat,
    TelegramChatGroup,
    TelegramChatGroupClub,
)


class GroupType(SimpleListFilter):
    """
    This filter is being used in wagtail admin panel in member model. !notimplemented
    """

    title = "has telegram username"
    parameter_name = "Grouptype__has"

    def lookups(self, request, model_admin):
        return (
            ("1", "Yes"),
            ("0", "No"),
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value() == "1":
            return queryset.filter().exclude(
                Q(telegram_username__isnull=True) | Q(telegram_username__exact="")
            )
        elif self.value() == "0":
            return queryset.filter(
                Q(telegram_username__isnull=True) | Q(telegram_username__exact="")
            )


class TelegramChatAdmin(ModelAdmin):
    model = TelegramChat
    menu_label = "Chats"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the user overview
    list_display = ("chat_id",)
    search_fields = ("chat_id",)


class TelegramChatGroupAdmin(ModelAdmin):
    model = TelegramChatGroup
    menu_label = "Groups"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the user overview
    list_display = ("chat_id",)
    search_fields = ("chat_id",)


class TelegramChatGroupClubAdmin(ModelAdmin):
    model = TelegramChatGroupClub
    menu_label = "Groups"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the user overview
    list_display = ("chat_id",)
    # list_filter = (GroupType)
    search_fields = ("chat_id",)


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
