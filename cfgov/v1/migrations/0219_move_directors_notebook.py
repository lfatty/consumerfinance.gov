# Generated by Django 2.2.12 on 2020-06-02 16:41

import v1.atomic_elements.molecules
import v1.blocks
import v1.models.snippets
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0218_add_force_breadcrumbs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfgovpage',
            name='sidefoot',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('slug_text', wagtail.core.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')]))]))])), ('related_links', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))])), ('related_posts', wagtail.core.blocks.StructBlock([('limit', wagtail.core.blocks.CharBlock(default='3', help_text='This limit applies to EACH TYPE of post this module retrieves, not the total number of retrieved posts.')), ('show_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text='This toggles the heading and icon for the related types.', label='Show Heading and Icon?', required=False)), ('header_title', wagtail.core.blocks.CharBlock(default='Further reading', label='Slug Title')), ('relate_posts', wagtail.core.blocks.BooleanBlock(default=True, editable=False, label='Blog Posts', required=False)), ('relate_newsroom', wagtail.core.blocks.BooleanBlock(default=True, editable=False, label='Newsroom', required=False)), ('relate_events', wagtail.core.blocks.BooleanBlock(default=True, label='Events', required=False)), ('specific_categories', wagtail.core.blocks.ListBlock(wagtail.core.blocks.ChoiceBlock(choices=[('Blog', (('At the CFPB', 'At the CFPB'), ("Director's notebook", "Director's notebook"), ('Policy &amp; Compliance', 'Policy and compliance'), ('Data, Research &amp; Reports', 'Data, research, and reports'), ('Info for Consumers', 'Info for consumers'))), ('Newsroom', (('Op-Ed', 'Op-ed'), ('Press Release', 'Press release'), ('Speech', 'Speech'), ('Testimony', 'Testimony')))], required=False), required=False)), ('and_filtering', wagtail.core.blocks.BooleanBlock(default=False, help_text='If checked, related posts will only be pulled in if they match ALL topic tags set on this page. Otherwise, related posts can match any one topic tag.', label='Match all topic tags', required=False)), ('alternate_view_more_url', wagtail.core.blocks.CharBlock(help_text='By default, the "View more" link will go to the Activity Log, filtered based on the above parameters. Enter a URL in this field to override that link destination.', label='Alternate "View more" URL', required=False))])), ('related_metadata', wagtail.core.blocks.StructBlock([('slug', wagtail.core.blocks.CharBlock(max_length=100)), ('content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('blob', wagtail.core.blocks.RichTextBlock())], icon='pilcrow')), ('list', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock(default='/', required=False))])))], icon='list-ul')), ('date', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(max_length=100)), ('date', wagtail.core.blocks.DateBlock())], icon='date')), ('topics', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Topics', max_length=100)), ('show_topics', wagtail.core.blocks.BooleanBlock(default=True, required=False))], icon='tag')), ('categories', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Categories', max_length=100)), ('show_categories', wagtail.core.blocks.BooleanBlock(default=True, required=False))], icon='list-ul'))])), ('is_half_width', wagtail.core.blocks.BooleanBlock(default=False, required=False))])), ('email_signup', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.core.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.core.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.core.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))])), ('sidebar_contact', wagtail.core.blocks.StructBlock([('contact', wagtail.snippets.blocks.SnippetChooserBlock('v1.Contact')), ('has_top_rule_line', wagtail.core.blocks.BooleanBlock(default=False, help_text='Add a horizontal rule line to top of contact block.', required=False))])), ('rss_feed', v1.atomic_elements.molecules.RSSFeed()), ('social_media', wagtail.core.blocks.StructBlock([('is_share_view', wagtail.core.blocks.BooleanBlock(default=True, help_text='If unchecked, social media icons will link users to official CFPB accounts. Do not fill in any further fields.', label='Desired action: share this page', required=False)), ('blurb', wagtail.core.blocks.CharBlock(default="Look what I found on the CFPB's site!", help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False)), ('twitter_text', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom text for Twitter shares. If blank, will default to value of blurb field above.', max_length=100, required=False)), ('twitter_related', wagtail.core.blocks.CharBlock(help_text='(Optional) A comma-separated list of accounts related to the content of the shared URL. Do not enter the  @ symbol. If blank, it will default to just "cfpb".', required=False)), ('twitter_hashtags', wagtail.core.blocks.CharBlock(help_text='(Optional) A comma-separated list of hashtags to be appended to default tweet text.', required=False)), ('twitter_lang', wagtail.core.blocks.CharBlock(help_text='(Optional) Loads text components in the specified language, if other than English. E.g., use "es"  for Spanish. See https://dev.twitter.com/web/overview/languages for a list of supported language codes.', required=False)), ('email_title', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom subject for email shares. If blank, will default to value of blurb field above.', required=False)), ('email_text', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom text for email shares. If blank, will default to "Check out this page from the CFPB".', required=False)), ('email_signature', wagtail.core.blocks.CharBlock(help_text='(Optional) Adds a custom signature line to email shares. ', required=False)), ('linkedin_title', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom title for LinkedIn shares. If blank, will default to value of blurb field above.', required=False)), ('linkedin_text', wagtail.core.blocks.CharBlock(help_text='(Optional) Custom text for LinkedIn shares.', required=False))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))], blank=True),
        ),
        migrations.AlterField(
            model_name='cfgovpagecategory',
            name='name',
            field=models.CharField(choices=[('Administrative adjudication docket', (('administrative-adjudication', 'Administrative adjudication'), ('stipulation-and-constent-order', 'Stipulation and consent order'))), ('Amicus Brief', (('us-supreme-court', 'U.S. Supreme Court'), ('fed-circuit-court', 'Federal Circuit Court'), ('fed-district-court', 'Federal District Court'), ('state-court', 'State Court'))), ('Blog', (('at-the-cfpb', 'At the CFPB'), ('directors-notebook', "Director's notebook"), ('policy_compliance', 'Policy and compliance'), ('data-research-reports', 'Data, research, and reports'), ('info-for-consumers', 'Info for consumers'))), ('Consumer Reporting Companies', (('nationwide', 'Nationwide'), ('employment-screening', 'Employment screening'), ('tenant-screening', 'Tenant screening'), ('check-bank-screening', 'Check and bank screening'), ('personal-property-insurance', 'Personal property insurance'), ('medical', 'Medical'), ('low-income-and-subprime', 'Low-income and subprime'), ('supplementary-reports', 'Supplementary reports'), ('utilities', 'Utilities'), ('retail', 'Retail'), ('gaming', 'Gaming'))), ('Enforcement Action', (('civil-action', 'Civil Action'), ('administrative-proceeding', 'Administrative Proceeding'))), ('Final rule', (('interim-final-rule', 'Interim final rule'), ('final-rule', 'Final rule'))), ('FOIA Frequently Requested Record', (('report', 'Report'), ('log', 'Log'), ('record', 'Record'))), ('Implementation Resource', (('compliance-aid', 'Compliance aid'), ('official-guidance', 'Official guidance'))), ('Newsroom', (('op-ed', 'Op-ed'), ('press-release', 'Press release'), ('speech', 'Speech'), ('testimony', 'Testimony'))), ('Notice and Opportunity for Comment', (('notice-proposed-rule', 'Advance notice of proposed rulemaking'), ('proposed-rule', 'Proposed rule'), ('interim-final-rule-2', 'Interim final rule'), ('request-comment-info', 'Request for comment or information'), ('proposed-policy', 'Proposed policy'), ('intent-preempt-determ', 'Intent to make preemption determination'), ('info-collect-activity', 'Information collection activities'), ('notice-privacy-act', 'Notice related to Privacy Act'))), ('Research Report', (('consumer-complaint', 'Consumer complaint'), ('super-highlight', 'Supervisory Highlights'), ('data-point', 'Data point'), ('industry-markets', 'Industry and markets'), ('consumer-edu-empower', 'Consumer education and empowerment'), ('to-congress', 'To Congress'))), ('Rule Under Development', (('notice-proposed-rule-2', 'Advance notice of proposed rulemaking'), ('proposed-rule-2', 'Proposed rule'))), ('Story', (('auto-loans', 'Auto loans'), ('bank-accts-services', 'Bank accounts and services'), ('credit-cards', 'Credit cards'), ('credit-reports-scores', 'Credit reports and scores'), ('debt-collection', 'Debt collection'), ('money-transfers', 'Money transfers'), ('mortgages', 'Mortgages'), ('payday-loans', 'Payday loans'), ('prepaid-cards', 'Prepaid cards'), ('student-loans', 'Student loans')))], max_length=255),
        ),
        migrations.AlterField(
            model_name='sublandingpage',
            name='sidebar_breakout',
            field=wagtail.core.fields.StreamField([('slug', wagtail.core.blocks.CharBlock(icon='title')), ('heading', wagtail.core.blocks.CharBlock(icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='edit')), ('breakout_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('is_round', wagtail.core.blocks.BooleanBlock(default=True, label='Round?', required=False)), ('icon', wagtail.core.blocks.CharBlock(help_text='Enter icon class name.')), ('heading', wagtail.core.blocks.CharBlock(label='Introduction Heading', required=False)), ('body', wagtail.core.blocks.TextBlock(label='Introduction Body', required=False))], heading='Breakout Image', icon='image')), ('related_posts', wagtail.core.blocks.StructBlock([('limit', wagtail.core.blocks.CharBlock(default='3', help_text='This limit applies to EACH TYPE of post this module retrieves, not the total number of retrieved posts.')), ('show_heading', wagtail.core.blocks.BooleanBlock(default=True, help_text='This toggles the heading and icon for the related types.', label='Show Heading and Icon?', required=False)), ('header_title', wagtail.core.blocks.CharBlock(default='Further reading', label='Slug Title')), ('relate_posts', wagtail.core.blocks.BooleanBlock(default=True, editable=False, label='Blog Posts', required=False)), ('relate_newsroom', wagtail.core.blocks.BooleanBlock(default=True, editable=False, label='Newsroom', required=False)), ('relate_events', wagtail.core.blocks.BooleanBlock(default=True, label='Events', required=False)), ('specific_categories', wagtail.core.blocks.ListBlock(wagtail.core.blocks.ChoiceBlock(choices=[('Blog', (('At the CFPB', 'At the CFPB'), ("Director's notebook", "Director's notebook"), ('Policy &amp; Compliance', 'Policy and compliance'), ('Data, Research &amp; Reports', 'Data, research, and reports'), ('Info for Consumers', 'Info for consumers'))), ('Newsroom', (('Op-Ed', 'Op-ed'), ('Press Release', 'Press release'), ('Speech', 'Speech'), ('Testimony', 'Testimony')))], required=False), required=False)), ('and_filtering', wagtail.core.blocks.BooleanBlock(default=False, help_text='If checked, related posts will only be pulled in if they match ALL topic tags set on this page. Otherwise, related posts can match any one topic tag.', label='Match all topic tags', required=False)), ('alternate_view_more_url', wagtail.core.blocks.CharBlock(help_text='By default, the "View more" link will go to the Activity Log, filtered based on the above parameters. Enter a URL in this field to override that link destination.', label='Alternate "View more" URL', required=False))])), ('job_listing_list', wagtail.core.blocks.StructBlock([('more_jobs_page', wagtail.core.blocks.PageChooserBlock(help_text='Link to full list of jobs'))]))], blank=True),
        ),
    ]
