from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock

from wagtailtrans.models import TranslatablePage

from agrihub.blocks import PersonVCards, Cards4xn, PartnerVCards


class FlexPage(TranslatablePage):
    """flexible content page with streamfields"""

    image = models.ForeignKey("wagtailimages.Image",
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL,
                              related_name="+",
                              help_text="Shown in jumbotron"
                              )

    body = StreamField([
        ('header', HeaderBlock()),
        ('paragraph', blocks.RichTextBlock(features=[
            'bold', 'italic', 'link', 'document-link', 'code', 'blockquote'])),
        ('list', ListBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('chart', ChartBlock()),
        ('map', MapBlock()),
        ('image_slider', ImageSliderBlock()),
        ('person_vcards', PersonVCards()),
        ('misc_cards', Cards4xn()),
        ('partner_vcards', PartnerVCards()),
    ], blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel("image"),
        StreamFieldPanel("body", classname="Full"),
    ]


    class Meta:
        verbose_name = "FlexPage"
        verbose_name_plural = "FlexPages"
        # template = "flex/flex_page.html"
