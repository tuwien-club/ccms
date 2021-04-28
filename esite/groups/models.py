from django.db import models
from bifrost.decorators import login_required
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import StreamField
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
class GroupPage(BasePage):
    body = StreamField(StreamFieldBlock())

    content_panels = BasePage.content_panels + [StreamFieldPanel("body")]

    graphql_fields = [
        GraphQLString(
            "slug",
            publisher_options=PublisherOptions(read=True, update=True, create=True),
            required=True,
        ),
        GraphQLString(
            "title",
            publisher_options=PublisherOptions(read=True, update=True, create=True),
            required=True,
        ),
        GraphQLString(
            "date",
            publisher_options=PublisherOptions(read=True, update=True, create=True),
            required=True,
        ),
        GraphQLStreamfield("body",
            #publisher_options=PublisherOptions(read=True, update=True, create=True),
            #required=True,
        ),
    ]
