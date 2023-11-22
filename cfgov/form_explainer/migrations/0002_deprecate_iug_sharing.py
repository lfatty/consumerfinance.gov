# Generated by Django 3.2.20 on 2023-09-05 21:21

from django.db import migrations
import v1.blocks
import wagtail.blocks
import wagtail.contrib.typed_table_block.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('form_explainer', '0001_squashed_0008_new_table_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formexplainerpage',
            name='content',
            field=wagtail.fields.StreamField([('explainer', wagtail.blocks.StructBlock([('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], label='Heading (optional)', required=False)), ('pages', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(icon='image', required=True)), ('categories', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Optional. Leave blank if there is only one type of note for this image.', label='Category title', required=False)), ('notes', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(label='Expandable header', required=True)), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], label='Expandable text', required=True)), ('coordinates', wagtail.blocks.StructBlock([('left', wagtail.blocks.FloatBlock(label='X value (in percentage)', max_value=100, min_value=0, required=True)), ('top', wagtail.blocks.FloatBlock(label='Y value (in percentage)', max_value=100, min_value=0, required=True)), ('width', wagtail.blocks.FloatBlock(label='Width (in percentage)', max_value=100, min_value=0, required=True)), ('height', wagtail.blocks.FloatBlock(label='Height (in percentage)', max_value=100, min_value=0, required=True))], form_classname='coordinates', help_text='Enter percentage values for the highlighted area of the image associated with this expandable. See <a href="https://github.cfpb.gov/CFPB/hubcap/wiki/Form-explainer-page#add-image-coordinates">Hubcap documentation</a> for more information on identifying coordinates.', label='Image coordinates'))], form_classname='explainer_notes', required=False), default=[]))], required=False)))], required=False)))])), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))])), ('info_unit_group', wagtail.blocks.StructBlock([('format', wagtail.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.blocks.RichTextBlock(required=False)), ('link_image_and_heading', wagtail.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('border_radius_image', wagtail.blocks.ChoiceBlock(choices=[('none', 'None'), ('rounded', 'Rounded corners'), ('circle', 'Circle')], help_text='Adds a <em>border-radius</em> class to images in this group, allowing for a rounded or circular border.', label='Border radius for images?', required=False)), ('info_units', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False))]), required=False))]), default=[]))])), ('full_width_text', wagtail.blocks.StreamBlock([('content', wagtail.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.blocks.StructBlock([('content_block', wagtail.blocks.RichTextBlock()), ('anchor_link', wagtail.blocks.StructBlock([('link_id', wagtail.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False))]))])), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('image_width', wagtail.blocks.ChoiceBlock(choices=[('full', 'Full width'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))])), ('table', wagtail.blocks.StructBlock([('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', wagtail.blocks.CharBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('options', wagtail.blocks.MultipleChoiceBlock(choices=[('is_full_width', 'Display the table at full width'), ('stack_on_mobile', 'Stack the table columns on mobile')], required=False)), ('data', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.blocks.CharBlock()), ('numeric', wagtail.blocks.FloatBlock()), ('rich_text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link', 'superscript']))]))])), ('quote', wagtail.blocks.StructBlock([('body', wagtail.blocks.TextBlock()), ('citation', wagtail.blocks.TextBlock(required=False)), ('is_large', wagtail.blocks.BooleanBlock(required=False))])), ('cta', wagtail.blocks.StructBlock([('slug_text', wagtail.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('paragraph', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False))])))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', v1.blocks.EmailSignUpChooserBlock()), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))]))]))], use_json_field=True),
        ),
    ]
