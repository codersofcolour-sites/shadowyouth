from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable

from streams import blocks

class HomePage(Page):
    templates = "home/hompage_page.html"
    banner_title = models.CharField(max_length = 100, blank = False, null = True)
    banner_subtitle = RichTextField(features = ["bold", "italic", "center"], null = True, blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null = True,
        blank = True,
        on_delete =models.SET_NULL,
        related_name = "+",
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",  
        null = True,
        blank = True,
        on_delete =models.SET_NULL,
        related_name = "+",
    )
    content = StreamField([("cta", blocks.CTABlock())], null=True, blank=True)
    
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
        ],
        default="",
        blank=True,
    )
    
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
                StreamFieldPanel("content"),
            ],
            heading="Banner Options",
        
        ),
       
    ]
    
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"