from django.db import models
from bifrost.decorators import login_required
from modelcluster.fields import ParentalKey
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtailmedia.edit_handlers import MediaChooserPanel
from bifrost.api.models import (
    GraphQLCollection,
    GraphQLDocument,
    GraphQLForeignKey,
    GraphQLImage,
    GraphQLMedia,
    GraphQLPage,
    GraphQLSnippet,
    GraphQLStreamfield,
    GraphQLString,
)
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    PageChooserPanel,
    StreamFieldPanel,
    TabbedInterface,
)
from bifrost.publisher.actions import register_publisher
from bifrost.publisher.options import PublisherOptions

from esite.utils.models import BasePage
from .blocks import StreamFieldBlock


@register_publisher(
    read_singular=True,
    create=True,
    update=True,
    delete=True,
    read_singular_permission=login_required,
)
class HowtoPage(BasePage):
    template = "patterns/pages/home/home_page.html"

    # Only allow creating HomePages at the root level
    parent_page_types = ["home.HomePage"]
    # subpage_types = []

    class Meta:
        verbose_name = "HowTo Page"

    body = StreamField(StreamFieldBlock())

    graphql_fields = [
        GraphQLString(
            "slug",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "title",
            required=True,
            publisher_options=PublisherOptions(
                create=True, update=True, read=True, delete=True
            ),
        ),
        GraphQLStreamfield(
            "body",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
    ]

    content_panels = BasePage.content_panels + [
        StreamFieldPanel("body"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(
                BasePage.promote_panels + BasePage.settings_panels,
                heading="Settings",
                classname="settings",
            ),
        ]
    )
