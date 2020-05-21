from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


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

    # later content as streamfields
    blogContent = models.TextField(null=True, blank=False)
    content_panels = Page.content_panels + [
        FieldPanel("blogTeaser"),
        FieldPanel("blogContent"),
        ImageChooserPanel("blogImage"),
    ]


class Meta:
    verbose_name = "Blogpost"
    verbose_name_plural = "Blogposts"


class BlogListingPage(Page):
    """Liste der Blogposts"""
    max_count_per_parent = 1

    class Meta:
        verbose_name = "Blogliste"
        verbose_name_plural = "Blogposts"
