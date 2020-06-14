from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock


class BlogPage(Page):
    """Einzelner Blogpost"""
    # title wird geerbt
    blogTeaser = models.CharField(max_length=50, null=True, blank=False)
    blogImage = models.ForeignKey("wagtailimages.Image",
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL,
                                  related_name="+",
                                  help_text="this image will be displayed in the listing page and gets cropped to "
                                            "300x200 "
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
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("blogTeaser"),
        ImageChooserPanel("blogImage"),
        StreamFieldPanel("body", classname="Full"),
    ]


class Meta:
    verbose_name = "Blogpost"
    verbose_name_plural = "Blogposts"


class BlogListingPage(Page):
    """Liste der Blogposts"""
    max_count_per_parent = 1

    # add blogposts as children to contexts
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = self.get_children().filter(
            live=True)

        return context

    class Meta:
        verbose_name = "Blogliste"
        verbose_name_plural = "Blogposts"
