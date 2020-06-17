from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ImageSliderBlock

from agrihub.blocks import Announcement, Cards4xn
from wagtailtrans.models import TranslatablePage


class HomePage(TranslatablePage):
    """Die Willkommensseite"""

    jumbotronTitle = models.CharField(max_length=30, blank=False, null=True)
    jumbotronSubtitle = models.CharField(max_length=200, blank=False, null=True)
    jumbotronImage = models.ForeignKey("wagtailimages.Image",
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       related_name="+")


    announcements = StreamField([
        ('announcement', Announcement()),
    ], blank=True)

    body = StreamField([
        ('header', HeaderBlock()),
        ('paragraph', blocks.RichTextBlock(features=[
            'bold', 'italic', 'link', 'document-link', 'code', 'blockquote'])),
        ('list', ListBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('image_slider', ImageSliderBlock()),
        ('misc_card', Cards4xn()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("jumbotronTitle"),
        FieldPanel("jumbotronSubtitle"),
        ImageChooserPanel("jumbotronImage"),
        StreamFieldPanel("announcements", classname="Full"),
        StreamFieldPanel("body", classname="Full"),
    ]


    max_count = 1
