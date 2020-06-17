# Generated by Django 3.0.6 on 2020-06-17 08:03

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailtrans', '0009_create_initial_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('jumbotronTitle', models.CharField(max_length=30, null=True)),
                ('jumbotronSubtitle', models.CharField(max_length=200, null=True)),
                ('announcements', wagtail.core.fields.StreamField([('announcement', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Title', required=True)), ('type', wagtail.core.blocks.ChoiceBlock(choices=[('info', 'info'), ('danger', 'danger'), ('primary', 'primary'), ('secondary', 'secondary'), ('dark', 'dark')], help_text='bootstrap4 alert-type class')), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h5', 'ol', 'ul', 'hr', 'link', 'document-link'], help_text='text', required=True))]))], blank=True)),
                ('body', wagtail.core.fields.StreamField([('header', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.ChoiceBlock(choices=[('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], label='Header Size')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=50))])), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link', 'code', 'blockquote'])), ('list', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(), label='Items'))])), ('image_text_overlay', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200))])), ('cropped_images_with_text', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200))]), label='Image Item'))])), ('list_with_images', wagtail.core.blocks.StructBlock([('list_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('title', wagtail.core.blocks.CharBlock(label='Title', max_length=200)), ('text', wagtail.core.blocks.CharBlock(label='Text', max_length=200)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=200, required=False)), ('link_url', wagtail.core.blocks.URLBlock(label='Link URL', max_length=200, required=False))]), label='List Item'))])), ('thumbnail_gallery', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image'))]), label='Image'))])), ('image_slider', wagtail.core.blocks.StructBlock([('image_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image'))]), label='Image'))])), ('misc_card', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add cards title', required=False)), ('text', wagtail.core.blocks.TextBlock(help_text='Write a short (350 characters) text', max_length=350, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add a profile picture rendered in card', required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='Add a link to the card', required=False))])))]))], blank=True)),
                ('jumbotronImage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage',),
        ),
    ]
