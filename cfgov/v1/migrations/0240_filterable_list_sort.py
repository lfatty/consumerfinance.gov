# Generated by Django 3.2.18 on 2023-05-15 17:45

from django.db import migrations
import v1.atomic_elements.tables
import v1.blocks
import v1.util.ref
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0239_field_cleanup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsefilterablepage',
            name='content',
            field=wagtail.fields.StreamField([('full_width_text', wagtail.blocks.StreamBlock([('content', wagtail.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.blocks.StructBlock([('content_block', wagtail.blocks.RichTextBlock()), ('anchor_link', wagtail.blocks.StructBlock([('link_id', wagtail.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False))]))])), ('heading', wagtail.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('image_width', wagtail.blocks.ChoiceBlock(choices=[('full', 'Full width'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))])), ('table_block', v1.atomic_elements.tables.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.blocks.StructBlock([('body', wagtail.blocks.TextBlock()), ('citation', wagtail.blocks.TextBlock(required=False)), ('is_large', wagtail.blocks.BooleanBlock(required=False))])), ('cta', wagtail.blocks.StructBlock([('slug_text', wagtail.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('paragraph', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False))])))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', v1.blocks.EmailSignUpChooserBlock()), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))]))])), ('filter_controls', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(required=False)), ('is_bordered', wagtail.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.blocks.BooleanBlock(required=False)), ('no_posts_message', wagtail.blocks.CharBlock(help_text='Message for the <a href="https://cfpb.github.io/design-system/components/notifications#default-base-notification">notification</a> that will be displayed instead of filter controls if there are no posts to filter.', required=False)), ('no_posts_explanation', wagtail.blocks.CharBlock(help_text='Additional explanation for the notification that will be displayed if there are no posts to filter.', required=False)), ('post_date_description', wagtail.blocks.CharBlock(help_text='Strongly encouraged to help users understand the action that the date of the post is linked to, i.e. published, issued, released.', label='Date stamp descriptor', required=False)), ('title', wagtail.blocks.BooleanBlock(default=True, help_text='Whether to include a "Search by keyword" filter in the filter controls.', label='Filter by keyword', required=False)), ('categories', wagtail.blocks.StructBlock([('filter_category', wagtail.blocks.BooleanBlock(default=True, help_text='Whether to include a "Category" filter in the filter controls.', label='Filter by Category', required=False)), ('show_preview_categories', wagtail.blocks.BooleanBlock(default=True, required=False)), ('page_type', wagtail.blocks.ChoiceBlock(choices=v1.util.ref.filterable_list_page_types, required=False))])), ('topic_filtering', wagtail.blocks.ChoiceBlock(choices=[('no_filter', "Don't filter topics"), ('sort_alphabetically', 'Filter topics, sort topic list alphabetically'), ('sort_by_frequency', 'Filter topics, sort topic list by number of results')], help_text='Whether to include a "Topics" filter in the filter controls')), ('ordering', wagtail.blocks.ChoiceBlock(choices=[('-start_date', 'Date'), ('title.raw', 'Alphabetical')], help_text='How to order results')), ('statuses', wagtail.blocks.BooleanBlock(default=False, help_text='Whether to include a "Status" filter in the filter controls. Only enable if using on an enforcement actions filterable list.', label='Filter by Enforcement Statuses', required=False)), ('products', wagtail.blocks.BooleanBlock(default=False, help_text='Whether to include a "Product" filter in the filter controls. Only enable if using on an enforcement actions filterable list.', label='Filter by Enforcement Products', required=False)), ('language', wagtail.blocks.BooleanBlock(default=False, help_text='Whether to include a "Language" filter in the filter controls.Only enable if there are non-english filterable results available.', label='Filter by Language', required=False)), ('date_range', wagtail.blocks.BooleanBlock(default=True, help_text='Whether to include a set of "Date range" filters in the filter controls.', label='Filter by Date Range', required=False)), ('output_5050', wagtail.blocks.BooleanBlock(default=False, label='Render preview items as 50-50s', required=False)), ('link_image_and_heading', wagtail.blocks.BooleanBlock(default=False, help_text='Add links to post preview images and headings in filterable list results', required=False)), ('filter_children', wagtail.blocks.BooleanBlock(default=True, help_text='If checked this list will only filter its child pages.', required=False))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='sublandingfilterablepage',
            name='content',
            field=wagtail.fields.StreamField([('text_introduction', wagtail.blocks.StructBlock([('eyebrow', wagtail.blocks.CharBlock(help_text='Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', label='Pre-heading', required=False)), ('heading', wagtail.blocks.CharBlock(required=False)), ('intro', wagtail.blocks.RichTextBlock(required=False)), ('body', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False))]), required=False)), ('has_rule', wagtail.blocks.BooleanBlock(help_text='Check this to add a horizontal rule line to bottom of text introduction.', label='Has bottom rule', required=False))])), ('full_width_text', wagtail.blocks.StreamBlock([('content', wagtail.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.blocks.StructBlock([('content_block', wagtail.blocks.RichTextBlock()), ('anchor_link', wagtail.blocks.StructBlock([('link_id', wagtail.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False))]))])), ('heading', wagtail.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('image_width', wagtail.blocks.ChoiceBlock(choices=[('full', 'Full width'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))])), ('table_block', v1.atomic_elements.tables.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.blocks.StructBlock([('body', wagtail.blocks.TextBlock()), ('citation', wagtail.blocks.TextBlock(required=False)), ('is_large', wagtail.blocks.BooleanBlock(required=False))])), ('cta', wagtail.blocks.StructBlock([('slug_text', wagtail.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=False)), ('paragraph', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False))])))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', v1.blocks.EmailSignUpChooserBlock()), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))]))])), ('filter_controls', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(required=False)), ('is_bordered', wagtail.blocks.BooleanBlock(required=False)), ('is_midtone', wagtail.blocks.BooleanBlock(required=False)), ('is_expanded', wagtail.blocks.BooleanBlock(required=False)), ('no_posts_message', wagtail.blocks.CharBlock(help_text='Message for the <a href="https://cfpb.github.io/design-system/components/notifications#default-base-notification">notification</a> that will be displayed instead of filter controls if there are no posts to filter.', required=False)), ('no_posts_explanation', wagtail.blocks.CharBlock(help_text='Additional explanation for the notification that will be displayed if there are no posts to filter.', required=False)), ('post_date_description', wagtail.blocks.CharBlock(help_text='Strongly encouraged to help users understand the action that the date of the post is linked to, i.e. published, issued, released.', label='Date stamp descriptor', required=False)), ('title', wagtail.blocks.BooleanBlock(default=True, help_text='Whether to include a "Search by keyword" filter in the filter controls.', label='Filter by keyword', required=False)), ('categories', wagtail.blocks.StructBlock([('filter_category', wagtail.blocks.BooleanBlock(default=True, help_text='Whether to include a "Category" filter in the filter controls.', label='Filter by Category', required=False)), ('show_preview_categories', wagtail.blocks.BooleanBlock(default=True, required=False)), ('page_type', wagtail.blocks.ChoiceBlock(choices=v1.util.ref.filterable_list_page_types, required=False))])), ('topic_filtering', wagtail.blocks.ChoiceBlock(choices=[('no_filter', "Don't filter topics"), ('sort_alphabetically', 'Filter topics, sort topic list alphabetically'), ('sort_by_frequency', 'Filter topics, sort topic list by number of results')], help_text='Whether to include a "Topics" filter in the filter controls')), ('ordering', wagtail.blocks.ChoiceBlock(choices=[('-start_date', 'Date'), ('title.raw', 'Alphabetical')], help_text='How to order results')), ('statuses', wagtail.blocks.BooleanBlock(default=False, help_text='Whether to include a "Status" filter in the filter controls. Only enable if using on an enforcement actions filterable list.', label='Filter by Enforcement Statuses', required=False)), ('products', wagtail.blocks.BooleanBlock(default=False, help_text='Whether to include a "Product" filter in the filter controls. Only enable if using on an enforcement actions filterable list.', label='Filter by Enforcement Products', required=False)), ('language', wagtail.blocks.BooleanBlock(default=False, help_text='Whether to include a "Language" filter in the filter controls.Only enable if there are non-english filterable results available.', label='Filter by Language', required=False)), ('date_range', wagtail.blocks.BooleanBlock(default=True, help_text='Whether to include a set of "Date range" filters in the filter controls.', label='Filter by Date Range', required=False)), ('output_5050', wagtail.blocks.BooleanBlock(default=False, label='Render preview items as 50-50s', required=False)), ('link_image_and_heading', wagtail.blocks.BooleanBlock(default=False, help_text='Add links to post preview images and headings in filterable list results', required=False)), ('filter_children', wagtail.blocks.BooleanBlock(default=True, help_text='If checked this list will only filter its child pages.', required=False))])), ('featured_content', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.TextBlock(help_text='Line breaks will be ignored.')), ('post', wagtail.blocks.PageChooserBlock(required=False)), ('show_post_link', wagtail.blocks.BooleanBlock(label='Render post link?', required=False)), ('post_link_text', wagtail.blocks.CharBlock(required=False)), ('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False))]), label='Additional Links')), ('video', wagtail.blocks.StructBlock([('video_id', wagtail.blocks.RegexBlock(error_messages={'invalid': 'The YouTube video ID is in the wrong format.'}, help_text='Enter the YouTube video ID, which is located at the end of the video URL, after "v=". For example, the video ID for https://www.youtube.com/watch?v=1V0Ax9OIc84 is 1V0Ax9OIc84.', label='YouTube video ID', regex='^[\\w-]{11}$', required=False)), ('thumbnail_image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional thumbnail image to show before and after the video plays. If the thumbnail image is not set here, the video player will default to showing the thumbnail that was set in (or automatically chosen by) YouTube.', required=False))], required=False))]))], use_json_field=True),
        ),
    ]
