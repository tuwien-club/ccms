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
class HomePage(BasePage):
    template = "patterns/pages/home/home_page.html"

    # Only allow creating HomePages at the root level
    parent_page_types = ["wagtailcore.Page"]
    # subpage_types = []

    class Meta:
        verbose_name = "Home Page"

    city = models.CharField(null=True, blank=False, max_length=255)
    zip_code = models.CharField(null=True, blank=False, max_length=255)
    address = models.CharField(null=True, blank=False, max_length=255)
    telephone = models.CharField(null=True, blank=False, max_length=255)
    telefax = models.CharField(null=True, blank=False, max_length=255)
    vat_number = models.CharField(null=True, blank=False, max_length=255)
    whatsapp_telephone = models.CharField(null=True, blank=True, max_length=255)
    whatsapp_contactline = models.CharField(null=True, blank=True, max_length=255)
    tax_id = models.CharField(null=True, blank=False, max_length=255)
    trade_register_number = models.CharField(null=True, blank=False, max_length=255)
    court_of_registry = models.CharField(null=True, blank=False, max_length=255)
    place_of_registry = models.CharField(null=True, blank=False, max_length=255)
    trade_register_number = models.CharField(null=True, blank=False, max_length=255)
    ownership = models.CharField(null=True, blank=False, max_length=255)
    email = models.CharField(null=True, blank=False, max_length=255)

    copyrightholder = models.CharField(null=True, blank=False, max_length=255)

    about = RichTextField(null=True, blank=False)
    privacy = RichTextField(null=True, blank=False)

    sociallinks = StreamField(
        [
            (
                "link",
                blocks.URLBlock(
                    help_text="Important! Format https://www.domain.tld/xyz"
                ),
            )
        ]
    )

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
            publisher_options=PublisherOptions(create=True, update=True, read=True, delete=True),
        ),
        GraphQLString(
            "date",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "city",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "zip_code",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "address",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "telephone",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "telefax",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "vat_number",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "whatsapp_telephone",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "whatsapp_contactline",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "tax_id",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "trade_register_number",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "court_of_registry",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "place_of_registry",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "ownership",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "email",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "copyrightholder",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "about",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLString(
            "privacy",
            required=True,
            publisher_options=PublisherOptions(create=True, update=True, read=True),
        ),
        GraphQLStreamfield("body"),
    ]

    content_panels = BasePage.content_panels+ [
        StreamFieldPanel("body"),
    ]

    imprint_panels = [
        MultiFieldPanel(
            [
                FieldPanel("city"),
                FieldPanel("zip_code"),
                FieldPanel("address"),
                FieldPanel("telephone"),
                FieldPanel("telefax"),
                FieldPanel("whatsapp_telephone"),
                FieldPanel("whatsapp_contactline"),
                FieldPanel("email"),
                FieldPanel("copyrightholder"),
            ],
            heading="contact",
        ),
        MultiFieldPanel(
            [
                FieldPanel("vat_number"),
                FieldPanel("tax_id"),
                FieldPanel("trade_register_number"),
                FieldPanel("court_of_registry"),
                FieldPanel("place_of_registry"),
                FieldPanel("trade_register_number"),
                FieldPanel("ownership"),
            ],
            heading="legal",
        ),
        StreamFieldPanel("sociallinks"),
        MultiFieldPanel(
            [FieldPanel("about"), FieldPanel("privacy")], heading="privacy"
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(imprint_panels, heading="Imprint"),
            ObjectList(
                BasePage.promote_panels + BasePage.settings_panels,
                heading="Settings",
                classname="settings",
            ),
        ]
    )