"""
from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup,
                                                modeladmin_register)


class CategoryModelAdmin(ModelAdmin):
    model = Category
    menu_icon = 'tag'


class PersonTypeModelAdmin(ModelAdmin):
    model = PersonType
    menu_icon = 'tag'



class TaxonomiesModelAdminGroup(ModelAdminGroup):
    menu_label = "Taxonomies"
    items = (
        CategoryModelAdmin,
        # PersonTypeModelAdmin,
    )
    menu_icon = 'tag'


modeladmin_register(TaxonomiesModelAdminGroup)
"""

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
