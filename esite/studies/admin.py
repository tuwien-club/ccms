from django.db.models import Q
from django.contrib.admin import SimpleListFilter
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from .models import Study


class StudyAdmin(ModelAdmin):
    model = Study
    menu_label = "Studies"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the user overview
    list_display = ("study_name", "study_type")
    list_filter = ("study_type",)
    search_fields = ("study_name", "study_type")

    # export_filename = 'people_spreadsheet'
    # list_export = ("date_joined", "matrikelnummer", "email", "telegram_username"),


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
