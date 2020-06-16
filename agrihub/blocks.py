from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


# 4gri Hub blocks for streamfields

class Announcement(blocks.StructBlock):
    """Block to render an announcement."""

    title = blocks.CharBlock(required=True, help_text="Title")
    type = blocks.ChoiceBlock(required=True, choices=[('info', 'info'),
                                                      ('danger', 'danger'),
                                                      ('primary', 'primary'),
                                                      ('secondary', 'secondary'),
                                                      ('dark', 'dark')],
                              help_text="bootstrap4 alert-type class")
    text = blocks.RichTextBlock(required=True, help_text="text",
                                features=['bold', 'italic', 'h5', 'ol', 'ul', 'hr', 'link', 'document-link'])

    class Meta:  # noqa
        template = "agrihub/announcement_block.html"
        icon = "warning"
        label = "Announcement"


class Card(blocks.StructBlock):
    """Block to render a full sized misc card."""

    title = blocks.CharBlock(required=True, help_text="Add cards title")
    text = blocks.TextBlock(required=True, help_text="Add cards text")
    image = ImageChooserBlock(required=False, help_text="Add a picture rendered in card")
    link = blocks.URLBlock(required=False, help_text="Add a link to the card")

    class Meta:  # noqa
        template = "agrihub/card_misc_block.html"
        icon = "doc-full"
        label = "misc fullsize card"

class Cards4xn(blocks.StructBlock):
    """A 4xn List of misc Cards."""

    cards = blocks.ListBlock(
            blocks.StructBlock(
                [

                    ("title", blocks.CharBlock(required=False, help_text="Add cards title")),
                    ("text", blocks.TextBlock(required=True, max_length=350,
                                                     help_text="Write a short (350 characters) text")),
                    ("image", ImageChooserBlock(required=False, help_text="Add a profile picture rendered in card")),
                    ("link", blocks.URLBlock(required=False, help_text="Add a link to the card")),
                ]
            )
        )

    class Meta:  # noqa
        template = "agrihub/cards_misc_4xn_block.html"
        icon = "doc-full"
        label = "4xn list of cards"


class PersonVCards(blocks.StructBlock):
    """A list of cards to render person vcards."""

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=False, help_text='Add your title eg. Prof.')),
                ("name", blocks.CharBlock(required=True, help_text="Add your name")),
                ("surname", blocks.CharBlock(required=True, help_text="Add your surname")),
                ("affiliation", blocks.CharBlock(required=False, help_text="Add your affilitations name")),
                ("image", ImageChooserBlock(required=True, help_text="Add a profile picture rendered in card")),
                ("orcid", blocks.CharBlock(required=False, help_text="Add your ORCID")),
                ("website", blocks.URLBlock(required=True, help_text="Add a link to you web profile")),
            ]
        )
    )

    class Meta:  # noqa
        template = "agrihub/vcards_persons_block.html"
        icon = "user"
        label = "List of vcards for Persons"


class PartnerVCards(blocks.StructBlock):
    """Block to render a partner vcards as listing."""

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("name", blocks.CharBlock(required=True, help_text="Add your name")),
                ("description", blocks.TextBlock(required=True, max_length=250,
                                                 help_text="Write a short (250 characters) description")),
                ("logo",
                 ImageChooserBlock(required=True, help_text="Institutions logo rendered in card cropped to 300x200")),
                ("website", blocks.URLBlock(required=True, help_text="link to institutions website")),
            ]
        )
    )

    class Meta:  # noqa
        template = "agrihub/vcards_partner_block.html"
        icon = "group"
        label = "List of vcards for partners"
