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
from bifrost.publisher.actions import register_publisher
from bifrost.publisher.options import PublisherOptions

from esite.utils.models import BasePage
from .blocks import StreamFieldBlock


@register_publisher(read_singular=True)
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


@register_publisher(read_singular=True)
class AuthorPage(BasePage):
    name = models.CharField(max_length=255)

    content_panels = BasePage.content_panels + [FieldPanel("name")]

    graphql_fields = [
        GraphQLString(
            "slug",
            publisher_options=PublisherOptions(read=True, create=True),
            required=True,
        ),
        GraphQLString(
            "title",
            publisher_options=PublisherOptions(read=True, create=True),
            required=True,
        ),
        GraphQLString(
            "date",
            publisher_options=PublisherOptions(read=True, create=True),
            required=True,
        ),
        GraphQLString(
            "name", publisher_options=PublisherOptions(read=True, create=True)
        ),
    ]


@register_publisher(read_singular=True)
class BlogPage(HeadlessPreviewMixin, BasePage):
    date = models.DateField("Post date")
    advert = models.ForeignKey(
        "home.Advert",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    cover = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    book_file = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    featured_media = models.ForeignKey(
        "wagtailmedia.Media",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    author = models.ForeignKey(
        AuthorPage, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    body = StreamField(StreamFieldBlock())

    content_panels = BasePage.content_panels + [
        FieldPanel("date"),
        ImageChooserPanel("cover"),
        StreamFieldPanel("body"),
        InlinePanel("related_links", label="Related links"),
        InlinePanel("authors", label="Authors"),
        FieldPanel("author"),
        SnippetChooserPanel("advert"),
        DocumentChooserPanel("book_file"),
        MediaChooserPanel("featured_media"),
    ]

    @property
    def copy(self):
        return self

    graphql_fields = [
        GraphQLString(
            "slug",
            required=True,
            publisher_options=PublisherOptions(create=True, read=True),
        ),
        GraphQLString(
            "title",
            required=True,
            publisher_options=PublisherOptions(create=True, read=True, delete=True),
        ),
        GraphQLString(
            "date",
            required=True,
            publisher_options=PublisherOptions(create=True, read=True),
        ),
        GraphQLString("date", required=True),
        GraphQLStreamfield("body"),
        GraphQLCollection(
            GraphQLForeignKey,
            "related_links",
            "home.blogpagerelatedlink",
            required=False,
            item_required=False,
            publisher_options=PublisherOptions(read=True, create=True, update=True),
        ),
        GraphQLCollection(GraphQLString, "related_urls", source="related_links.url"),
        GraphQLCollection(GraphQLString, "authors", source="authors.person.name"),
        GraphQLSnippet(
            "advert",
            "home.Advert",
            publisher_options=PublisherOptions(read=True, create=True),
        ),
        GraphQLImage(
            "cover", publisher_options=PublisherOptions(read=True, create=True)
        ),
        GraphQLDocument(
            "book_file", publisher_options=PublisherOptions(read=True, create=True)
        ),
        GraphQLMedia(
            "featured_media", publisher_options=PublisherOptions(read=True, create=True)
        ),
        GraphQLForeignKey(
            "copy", "home.BlogPage", publisher_options=PublisherOptions(read=True)
        ),
        GraphQLPage(
            "author", publisher_options=PublisherOptions(read=True, create=True)
        ),
    ]


@register_publisher(read_singular=True)
class BlogPageRelatedLink(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="related_links")
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [FieldPanel("name"), FieldPanel("url")]

    graphql_fields = [
        GraphQLPage("page", publisher_options=PublisherOptions(create=True, read=True)),
        GraphQLString(
            "name", publisher_options=PublisherOptions(read=True, create=True)
        ),
        GraphQLString(
            "url", publisher_options=PublisherOptions(read=True, create=True)
        ),
    ]


@register_publisher(read_singular=True)
class Person(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    panels = [FieldPanel("name"), FieldPanel("job")]

    graphql_fields = [
        GraphQLString(
            "name", publisher_options=PublisherOptions(create=True, delete=True)
        ),
        GraphQLString("job"),
    ]


@register_publisher(
    read_singular=True,
    read_plural=True,
    update=True,
    create=True,
    read_singular_permission=login_required,
)
class Author(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="authors")
    role = models.CharField(max_length=255)
    person = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )

    panels = [FieldPanel("role"), SnippetChooserPanel("person")]

    graphql_fields = [
        GraphQLPage(
            "page",
            publisher_options=PublisherOptions(create=True, read=True),
        ),
        GraphQLString(
            "role",
            publisher_options=PublisherOptions(
                create=True, read=True, update=True, readfilter=True
            ),
        ),
        GraphQLForeignKey(
            "person",
            Person,
            publisher_options=PublisherOptions(create=True, read=True, update=True),
        ),
    ]


@register_snippet
@register_publisher(read_singular=True)
class Advert(models.Model):
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [FieldPanel("url"), FieldPanel("text")]

    graphql_fields = [
        GraphQLString(
            "url", publisher_options=PublisherOptions(create=True, read=True)
        ),
        GraphQLString("text"),
    ]

    def __str__(self):
        return self.text


# @register_setting
# @register_publisher(read_singular=True)
# class SocialMediaSettings(BaseSetting):
#     facebook = models.URLField(help_text="Your Facebook page URL")
#     instagram = models.CharField(
#         max_length=255, help_text="Your Instagram username, without the @"
#     )
#     trip_advisor = models.URLField(help_text="Your Trip Advisor page URL")
#     youtube = models.URLField(help_text="Your YouTube channel or user account URL")

#     graphql_fields = [
#         GraphQLString("facebook"),
#         GraphQLString("instagram"),
#         GraphQLString("trip_advisor"),
#         GraphQLString("youtube"),
#     ]
