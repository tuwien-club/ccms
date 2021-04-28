from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from bifrost.api.helpers import register_streamfield_block
from bifrost.api.models import (
    GraphQLCollection,
    GraphQLEmbed,
    GraphQLForeignKey,
    GraphQLImage,
    GraphQLString,
)


@register_streamfield_block
class ImageGalleryImage(blocks.StructBlock):
    caption = blocks.CharBlock(classname="full title")
    image = ImageChooserBlock()

    graphql_fields = [GraphQLString("caption"), GraphQLImage("image")]


@register_streamfield_block
class ImageGalleryImages(blocks.StreamBlock):
    image = ImageGalleryImage()

    child_blocks = {"image": ImageGalleryImage}

    class Meta:
        min_num = 2
        max_num = 15


@register_streamfield_block
class ImageGalleryBlock(blocks.StructBlock):
    title = blocks.CharBlock(classname="full title")
    images = ImageGalleryImages()

    graphql_fields = [
        GraphQLString("title"),
        GraphQLCollection(GraphQLForeignKey, "images", ImageGalleryImage),
    ]


@register_streamfield_block
class VideoBlock(blocks.StructBlock):
    youtube_link = EmbedBlock(required=False)

    graphql_fields = [GraphQLEmbed("youtube_link")]


class StreamFieldBlock(blocks.StreamBlock):
    message = blocks.RichTextBlock()
    groups = blocks.ListBlock(blocks.RichTextBlock())

    graphql_fields = [
        GraphQLString("message"),
        GraphQLCollection(GraphQLString, "groups", blocks.RichTextBlock())
    ]
