from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):

    jumbotronTitle = models.CharField(max_length=30, blank= False, null= True)
    jumbotronSubtitle = models.CharField(max_length=200, blank= False, null= True)
    jumbotronImage = models.ForeignKey("wagtailimages.Image",
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       related_name="+")

    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel("jumbotronTitle"),
        FieldPanel("jumbotronSubtitle"),
        ImageChooserPanel("jumbotronImage"),
    ]
