from django import template

from esite.navigation.models import NavigationSettings

register = template.Library()


# Primary nav snippets
@register.inclusion_tag(
    "patterns/molecules/navigation/primarynav.html", takes_context=True
)
def primarynav(context):
    request = context["request"]
    return {
        "primarynav": NavigationSettings.for_site(request.site).primary_navigation,
        "request": request,
    }


# Secondary nav snippets
@register.inclusion_tag(
    "patterns/molecules/navigation/secondarynav.html", takes_context=True
)
def secondarynav(context):
    request = context["request"]
    return {
        "secondarynav": NavigationSettings.for_site(request.site).secondary_navigation,
        "request": request,
    }


# Sidebar nav snippets
@register.inclusion_tag(
    "patterns/molecules/navigation/sidebar.html", takes_context=True
)
def sidebar(context):
    return {
        "children": context["page"].get_children().live().public().in_menu(),
        "request": context["request"],
    }


# Footer links nav snippets
@register.inclusion_tag(
    "patterns/molecules/navigation/footerlinks.html", takes_context=True
)
def footerlinks(context):
    request = context["request"]
    return {
        "footerlinks": NavigationSettings.for_site(request.site).footer_links,
        "request": request,
    }


# Footer bottom nav snippets
@register.inclusion_tag(
    "patterns/molecules/navigation/footerbottomtext.html", takes_context=True
)
def footerbottomtext(context):
    request = context["request"]
    return {
        "footerbottomtext": NavigationSettings.for_site(
            request.site
        ).footer_bottom_text,
        "request": request,
    }


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
