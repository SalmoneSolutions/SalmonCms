from __future__ import unicode_literals
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import InlinePanel,FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from django.db import models

class HeroPage(Page):

    class ImageHero(blocks.StructBlock):
        hero_text = blocks.RichTextBlock(blank= True,required=False)
        hero_heading = blocks.CharBlock(required=False)
        link_text = blocks.CharBlock(required=False)
        link_location = blocks.CharBlock(required=False)
        hero_image = ImageChooserBlock()
        class Meta:
            icon='image'

    class TextHero(blocks.StructBlock):
        text = blocks.RichTextBlock(blank=True)
        class Meta:
            icon='placeholder'

    class ImageSliderHero(blocks.StructBlock):
         slide = blocks.StructBlock([
             ('Image',ImageChooserBlock()),
             ('Caption',  blocks.RichTextBlock(blank=True)),
         ])
         class Meta:
             icon='image'

    class FooterHero(blocks.StructBlock):
        footer_text = blocks.RichTextBlock(blank= True)
        footer_image = ImageChooserBlock()
        class Meta:
            icon='placeholder'

    body = StreamField([
            ('ImageHero',ImageHero()),
            ('TextHero',TextHero()),
            ('FooterHero', FooterHero()),
            ('ImageSlideHero', blocks.ListBlock(ImageSliderHero()))
        ],null=True,blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
