from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

# Register your models here.
from esite.members.admin import MemberAdmin
from esite.studies.admin import StudyAdmin
from esite.telegramchats.admin import (
    TelegramChatAdmin,
    TelegramChatGroupAdmin,
    TelegramChatGroupClubAdmin,
    TelegramChatGroupClubTopicAdmin,
    TelegramChatGroupClubStudyAdmin,
)


class ClubManagementAdmin(ModelAdminGroup):
    menu_label = "Club Management"
    menu_icon = "group"
    menu_order = 110
    add_to_settings_menu = False
    exclude_from_explorer = False
    items = (
        MemberAdmin,
        StudyAdmin,
        TelegramChatGroupClubTopicAdmin,
        TelegramChatGroupClubStudyAdmin,
    )


modeladmin_register(ClubManagementAdmin)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2020 miraculix-org Florian Kleber
