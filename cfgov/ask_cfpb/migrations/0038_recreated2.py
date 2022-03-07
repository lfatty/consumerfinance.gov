# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-20 16:24

import ask_cfpb.models.pages
import django.db.models.deletion
import modelcluster.fields
import v1.atomic_elements.molecules
import v1.atomic_elements.organisms
import v1.blocks
import v1.models.snippets
from django.conf import settings
from django.db import migrations, models
from wagtail.contrib.routable_page import models as routable_models
from wagtail.core import blocks as core_blocks
from wagtail.core import fields as core_fields
from wagtail.search import index
from wagtail.snippets import blocks as snippets_blocks


class Migration(migrations.Migration):

    replaces = [
        ('ask_cfpb', '0001_initial'),
        ('ask_cfpb', '0002_answeraudiencepage'),
        ('ask_cfpb', '0003_add_answercategorypage'),
        ('ask_cfpb', '0004_add_ask_category_images'),
        ('ask_cfpb', '0005_delete_answertagproxy'),
        ('ask_cfpb', '0006_update_help_text'),
        ('ask_cfpb', '0007_subcategory_prefixes'),
        ('ask_cfpb', '0008_fix_verbose_name_plural'),
        ('ask_cfpb', '0009_update_social_image_help_text'),
        ('ask_cfpb', '0010_answerpage_sidebar'),
        ('ask_cfpb', '0011_move_reusable_text_chooser_block'),
        ('ask_cfpb', '0012_add_rule_option_to_module'),
        ('ask_cfpb', '0013_recreated'),
        ('ask_cfpb', '0014_recreated_2'),
        ('ask_cfpb', '0015_update_email_signup_options'),
        ('ask_cfpb', '0016_modify_help_text_social_sharing_image'),
        ('ask_cfpb', '0017_adjust_fields_for_editing'),
        ('ask_cfpb', '0018_migrate_answer_field_help_text'),
        ('ask_cfpb', '0019_add_disclaimer_pagechooserblock_to_emailsignup'),
        ('ask_cfpb', '0020_rm_formfieldwithbutton'),
        ('ask_cfpb', '0021_rssfeed_improvements'),
        ('ask_cfpb', '0022_add_remaining_answer_fields_to_answer_page'),
        ('ask_cfpb', '0023_rename_snippet_to_short_answer'),
        ('ask_cfpb', '0024_add_portal_links_to_answerpage'),
        ('ask_cfpb', '0025_remove_answer_audience_page'),
        ('ask_cfpb', '0026_remove_redirect_to_and_answer_id_from_answer_page'),
        ('ask_cfpb', '0027_portalsearchpage'),
        ('ask_cfpb', '0028_answerpage_answer_content'),
        ('ask_cfpb', '0029_answer_schema_blocks'),
        ('ask_cfpb', '0030_remove_answer_category_page'),
        ('ask_cfpb', '0031_remove_deprecated_models_and_fields'),
        ('ask_cfpb', '0032_remove_html_editor'),
        ('ask_cfpb', '0033_add_article_page'),
        ('ask_cfpb', '0034_remove_answerresultspage_content'),
        ('ask_cfpb', '0035_move_glossaryterm'),
        ('ask_cfpb', '0036_auto_20191219_1445')
    ]

    dependencies = [
        ('ask_cfpb', '0037_recreated'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v1', '0198_recreated'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerLandingPage',
            fields=[
                ('landingpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.LandingPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.landingpage',),
        ),
        migrations.CreateModel(
            name='AnswerPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('last_edited', models.DateField(blank=True, help_text='Change the date to today if you make a significant change.', null=True)),
                ('question', models.TextField(blank=True)),
                ('statement', models.TextField(blank=True, help_text='(Optional) Use this field to rephrase the question title as a statement. Use only if this answer has been chosen to appear on a money topic portal (e.g. /consumer-tools/debt-collection).')),
                ('short_answer', core_fields.RichTextField(blank=True, help_text='Optional answer intro')),
                ('answer_content', core_fields.StreamField((('text', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text')),))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(features=['link', 'document-link'], label='Tip')),))), ('video_player', core_blocks.StructBlock((('video_url', core_blocks.RegexBlock(default='https://www.youtube.com/embed/', error_messages={'invalid': 'The YouTube URL is in the wrong format. You must use the embed URL (https://www.youtube.com/embed/video_id), which can be obtained by clicking Share > Embed on the YouTube video page.', 'required': 'The YouTube URL field is required for video players.'}, label='YouTube Embed URL', regex='^https:\\/\\/www\\.youtube\\.com\\/embed\\/.+$', required=True)),))), ('how_to_schema', core_blocks.StructBlock((('description', core_blocks.RichTextBlock(blank=True, features=['ol', 'ul', 'bold', 'italic', 'link', 'document-link'], required=False)), ('steps', core_blocks.ListBlock(core_blocks.StructBlock((('title', core_blocks.CharBlock(max_length=500)), ('step_content', core_blocks.StreamBlock((('text', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text')),))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(features=['link', 'document-link'], label='Tip')),))), ('video_player', core_blocks.StructBlock((('video_url', core_blocks.RegexBlock(default='https://www.youtube.com/embed/', error_messages={'invalid': 'The YouTube URL is in the wrong format. You must use the embed URL (https://www.youtube.com/embed/video_id), which can be obtained by clicking Share > Embed on the YouTube video page.', 'required': 'The YouTube URL field is required for video players.'}, label='YouTube Embed URL', regex='^https:\\/\\/www\\.youtube\\.com\\/embed\\/.+$', required=True)),))))))))))))), ('faq_schema', core_blocks.StructBlock((('description', core_blocks.RichTextBlock(blank=True, features=['ol', 'ul', 'bold', 'italic', 'link', 'document-link'], required=False)), ('questions', core_blocks.ListBlock(core_blocks.StructBlock((('question', core_blocks.CharBlock(max_length=500)), ('answer_content', core_blocks.StreamBlock((('text', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text')),))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', core_blocks.StructBlock((('content', core_blocks.RichTextBlock(features=['link', 'document-link'], label='Tip')),))), ('video_player', core_blocks.StructBlock((('video_url', core_blocks.RegexBlock(default='https://www.youtube.com/embed/', error_messages={'invalid': 'The YouTube URL is in the wrong format. You must use the embed URL (https://www.youtube.com/embed/video_id), which can be obtained by clicking Share > Embed on the YouTube video page.', 'required': 'The YouTube URL field is required for video players.'}, label='YouTube Embed URL', regex='^https:\\/\\/www\\.youtube\\.com\\/embed\\/.+$', required=True)),)))))))))))))), blank=True, verbose_name='Answer')),
                ('featured', models.BooleanField(default=False, help_text='Check to make this one of two featured answers on the landing page.')),
                ('featured_rank', models.IntegerField(blank=True, null=True)),
                ('search_tags', models.CharField(blank=True, help_text='Search words or phrases, separated by commas', max_length=1000)),
                ('user_feedback', core_fields.StreamField((('feedback', core_blocks.StructBlock((('was_it_helpful_text', core_blocks.CharBlock(default='Was this page helpful to you?', help_text='Use this field only for feedback forms that use "Was this helpful?" radio buttons.', required=False)), ('intro_text', core_blocks.CharBlock(help_text='Optional feedback intro', required=False)), ('question_text', core_blocks.CharBlock(help_text='Optional expansion on intro', required=False)), ('radio_intro', core_blocks.CharBlock(help_text='Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), ('radio_text', core_blocks.CharBlock(default='This information helps us understand your question better.', required=False)), ('radio_question_1', core_blocks.CharBlock(default='How soon do you expect to buy a home?', required=False)), ('radio_question_2', core_blocks.CharBlock(default='Do you currently own a home?', required=False)), ('button_text', core_blocks.CharBlock(default='Submit')), ('contact_advisory', core_blocks.RichTextBlock(help_text='Use only for feedback forms that ask for a contact email', required=False))))),), blank=True)),
                ('sidebar', core_fields.StreamField((('call_to_action', core_blocks.StructBlock((('slug_text', core_blocks.CharBlock(required=False)), ('paragraph_text', core_blocks.RichTextBlock(required=False)), ('button', core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False)), ('size', core_blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', core_blocks.StructBlock((('heading', core_blocks.CharBlock(required=False)), ('paragraph', core_blocks.RichTextBlock(required=False)), ('links', core_blocks.ListBlock(core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False))))))))), ('related_metadata', core_blocks.StructBlock((('slug', core_blocks.CharBlock(max_length=100)), ('content', core_blocks.StreamBlock((('text', core_blocks.StructBlock((('heading', core_blocks.CharBlock(max_length=100)), ('blob', core_blocks.RichTextBlock())), icon='pilcrow')), ('list', core_blocks.StructBlock((('heading', core_blocks.CharBlock(max_length=100)), ('links', core_blocks.ListBlock(core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False))))))), icon='list-ul')), ('date', core_blocks.StructBlock((('heading', core_blocks.CharBlock(max_length=100)), ('date', core_blocks.DateBlock())), icon='date')), ('topics', core_blocks.StructBlock((('heading', core_blocks.CharBlock(default='Topics', max_length=100)), ('show_topics', core_blocks.BooleanBlock(default=True, required=False))), icon='tag')), ('categories', core_blocks.StructBlock((('heading', core_blocks.CharBlock(default='Categories', max_length=100)), ('show_categories', core_blocks.BooleanBlock(default=True, required=False))), icon='list-ul'))))), ('is_half_width', core_blocks.BooleanBlock(default=False, required=False))))), ('email_signup', core_blocks.StructBlock((('heading', core_blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', core_blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', core_blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', core_blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', core_blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))), ('sidebar_contact', core_blocks.StructBlock((('contact', snippets_blocks.SnippetChooserBlock('v1.Contact')), ('has_top_rule_line', core_blocks.BooleanBlock(default=False, help_text='Add a horizontal rule line to top of contact block.', required=False))))), ('rss_feed', v1.atomic_elements.molecules.RSSFeed()), ('social_media', core_blocks.StructBlock((('is_share_view', core_blocks.BooleanBlock(default=True, help_text='If unchecked, social media icons will link users to official CFPB accounts. Do not fill in any further fields.', label='Desired action: share this page', required=False)), ('blurb', core_blocks.CharBlock(default="Look what I found on the CFPB's site!", help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False)), ('twitter_text', core_blocks.CharBlock(help_text='(Optional) Custom text for Twitter shares. If blank, will default to value of blurb field above.', max_length=100, required=False)), ('twitter_related', core_blocks.CharBlock(help_text='(Optional) A comma-separated list of accounts related to the content of the shared URL. Do not enter the  @ symbol. If blank, it will default to just "cfpb".', required=False)), ('twitter_hashtags', core_blocks.CharBlock(help_text='(Optional) A comma-separated list of hashtags to be appended to default tweet text.', required=False)), ('twitter_lang', core_blocks.CharBlock(help_text='(Optional) Loads text components in the specified language, if other than English. E.g., use "es"  for Spanish. See https://dev.twitter.com/web/overview/languages for a list of supported language codes.', required=False)), ('email_title', core_blocks.CharBlock(help_text='(Optional) Custom subject for email shares. If blank, will default to value of blurb field above.', required=False)), ('email_text', core_blocks.CharBlock(help_text='(Optional) Custom text for email shares. If blank, will default to "Check out this page from the CFPB".', required=False)), ('email_signature', core_blocks.CharBlock(help_text='(Optional) Adds a custom signature line to email shares. ', required=False)), ('linkedin_title', core_blocks.CharBlock(help_text='(Optional) Custom title for LinkedIn shares. If blank, will default to value of blurb field above.', required=False)), ('linkedin_text', core_blocks.CharBlock(help_text='(Optional) Custom text for LinkedIn shares.', required=False))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))), blank=True)),
                ('answer_base', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer_pages', to='ask_cfpb.Answer')),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.cfgovpage',),
        ),
        migrations.CreateModel(
            name='AnswerResultsPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.cfgovpage',),
        ),
        migrations.CreateModel(
            name='ArticleLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('text', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('category', models.CharField(choices=[('basics', 'Basics'), ('common_issues', 'Common issues'), ('howto', 'How to'), ('know_your_rights', 'Know your rights')], max_length=255)),
                ('heading', models.CharField(max_length=255)),
                ('intro', models.TextField()),
                ('inset_heading', models.CharField(blank=True, max_length=255, verbose_name='Heading')),
                ('sections', core_fields.StreamField((('section', core_blocks.StructBlock((('heading', core_blocks.CharBlock(label='Section heading', max_length=255, required=True)), ('summary', core_blocks.TextBlock(blank=True, label='Section summary', required=False)), ('link_text', core_blocks.CharBlock(blank=True, label='Section link text', required=False)), ('url', core_blocks.CharBlock(blank=True, label='Section link URL', max_length=255, required=False)), ('subsections', core_blocks.ListBlock(core_blocks.StructBlock((('heading', core_blocks.CharBlock(blank=True, label='Subsection heading', max_length=255, required=False)), ('summary', core_blocks.TextBlock(blank=True, label='Subsection summary', required=False)), ('link_text', core_blocks.CharBlock(label='Subsection link text', required=True)), ('url', core_blocks.CharBlock(label='Subsection link URL', required=True))))))))),))),
                ('sidebar', core_fields.StreamField((('call_to_action', core_blocks.StructBlock((('slug_text', core_blocks.CharBlock(required=False)), ('paragraph_text', core_blocks.RichTextBlock(required=False)), ('button', core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False)), ('size', core_blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', core_blocks.StructBlock((('heading', core_blocks.CharBlock(required=False)), ('paragraph', core_blocks.RichTextBlock(required=False)), ('links', core_blocks.ListBlock(core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False))))))))), ('related_metadata', core_blocks.StructBlock((('slug', core_blocks.CharBlock(max_length=100)), ('content', core_blocks.StreamBlock((('text', core_blocks.StructBlock((('heading', core_blocks.CharBlock(max_length=100)), ('blob', core_blocks.RichTextBlock())), icon='pilcrow')), ('list', core_blocks.StructBlock((('heading', core_blocks.CharBlock(max_length=100)), ('links', core_blocks.ListBlock(core_blocks.StructBlock((('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(default='/', required=False))))))), icon='list-ul')), ('date', core_blocks.StructBlock((('heading', core_blocks.CharBlock(max_length=100)), ('date', core_blocks.DateBlock())), icon='date')), ('topics', core_blocks.StructBlock((('heading', core_blocks.CharBlock(default='Topics', max_length=100)), ('show_topics', core_blocks.BooleanBlock(default=True, required=False))), icon='tag')), ('categories', core_blocks.StructBlock((('heading', core_blocks.CharBlock(default='Categories', max_length=100)), ('show_categories', core_blocks.BooleanBlock(default=True, required=False))), icon='list-ul'))))), ('is_half_width', core_blocks.BooleanBlock(default=False, required=False))))), ('email_signup', core_blocks.StructBlock((('heading', core_blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', core_blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', core_blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', core_blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', core_blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))), blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.cfgovpage',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_es', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='Do not edit this field')),
                ('slug_es', models.SlugField(help_text='Do not edit this field')),
                ('intro', core_fields.RichTextField(blank=True, help_text='Do not use H2, H3, H4, or H5 to style this text. Do not add links, images, videos or other rich text elements.')),
                ('intro_es', core_fields.RichTextField(blank=True, help_text='Do not use this field. It is not currently displayed on the front end.')),
                ('category_image', models.ForeignKey(blank=True, help_text='Select a custom image to appear when visitors share pages belonging to this category on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='v1.CFGOVImage')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GlossaryTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=255, verbose_name='TERM (ENGLISH)')),
                ('definition_en', core_fields.RichTextField(blank=True, null=True, verbose_name='DEFINITION (ENGLISH)')),
                ('anchor_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='ANCHOR SLUG (ENGLISH)')),
                ('name_es', models.CharField(blank=True, max_length=255, null=True, verbose_name='TERM (SPANISH)')),
                ('definition_es', core_fields.RichTextField(blank=True, null=True, verbose_name='DEFINITION (SPANISH)')),
                ('anchor_es', models.CharField(blank=True, max_length=255, null=True, verbose_name='ANCHOR SLUG (SPANISH)')),
                ('answer_page_en', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glossary_terms', to='ask_cfpb.AnswerPage', verbose_name='ANSWER PAGE (ENGLISH)')),
                ('answer_page_es', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glossary_terms_es', to='ask_cfpb.AnswerPage', verbose_name='ANSWER PAGE (SPANISH)')),
                ('portal_topic', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='glossary_terms', to='v1.PortalTopic')),
            ],
            bases=(index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='NextStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('show_title', models.BooleanField(default=False)),
                ('text', core_fields.RichTextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortalSearchPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('overview', models.TextField(blank=True)),
                ('portal_topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='portal_search_pages', to='v1.PortalTopic')),
            ],
            options={
                'abstract': False,
            },
            bases=(routable_models.RoutablePageMixin, ask_cfpb.models.pages.SecondaryNavigationJSMixin, 'v1.cfgovpage'),
        ),
        migrations.CreateModel(
            name='TagResultsPage',
            fields=[
                ('answerresultspage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ask_cfpb.AnswerResultsPage')),
            ],
            options={
                'abstract': False,
            },
            bases=(routable_models.RoutablePageMixin, 'ask_cfpb.answerresultspage'),
        ),
        migrations.AddField(
            model_name='articlelink',
            name='article_page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_links', to='ask_cfpb.ArticlePage'),
        ),
        migrations.AddField(
            model_name='answerpage',
            name='category',
            field=models.ManyToManyField(blank=True, help_text='Categorize this answer. Avoid putting into more than one category.', to='ask_cfpb.Category'),
        ),
        migrations.AddField(
            model_name='answerpage',
            name='portal_category',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='v1.PortalCategory'),
        ),
        migrations.AddField(
            model_name='answerpage',
            name='portal_topic',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='Limit to 1 portal topic if possible', to='v1.PortalTopic'),
        ),
        migrations.AddField(
            model_name='answerpage',
            name='primary_portal_topic',
            field=modelcluster.fields.ParentalKey(blank=True, help_text='Use only if assigning more than one portal topic, to control which topic is used as a breadcrumb.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_portal_topic', to='v1.PortalTopic'),
        ),
        migrations.AddField(
            model_name='answerpage',
            name='redirect_to_page',
            field=models.ForeignKey(blank=True, help_text='Choose another AnswerPage to redirect this page to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirect_to_pages', to='ask_cfpb.AnswerPage'),
        ),
        migrations.AddField(
            model_name='answerpage',
            name='related_questions',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='Maximum of 3 related questions', related_name='related_question', to='ask_cfpb.AnswerPage'),
        ),
        migrations.AddField(
            model_name='answerpage',
            name='related_resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='v1.RelatedResource'),
        ),
        migrations.AddField(
            model_name='answer',
            name='last_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='glossaryterm',
            unique_together=set([('portal_topic', 'name_en')]),
        ),
    ]
