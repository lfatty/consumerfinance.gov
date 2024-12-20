# Generated by Django 3.2.23 on 2024-01-11 14:14

from django.db import migrations

from wagtail.blocks.migrations.migrate_operation import MigrateStreamData

from v1.util.migrations import RegexAlterBlockValueOperation


# Regular expressions and operations that are common to all the page types
# in the migration.
ENTITY_SPAN_RE = (
    r"&lt;span id=&quot;"
    r"([\w -]+)"  # Group 1, the anchor id
    r"&quot;&gt;"
    r"((?:(?!&lt;/span&gt;).)*)"  # Group 2, everything contained within that
    # isn't attempting to close the "tag"
    r"&lt;/span&gt;"
)
REPLACEMENT_SPAN_RE = r'<span id="\1">\2</span>'

SPAN_OPERATION = RegexAlterBlockValueOperation(
    ENTITY_SPAN_RE, REPLACEMENT_SPAN_RE
)


class Migration(migrations.Migration):
    dependencies = [
        ("v1", "0018_ask_changes_202401"),
    ]

    operations = [
        MigrateStreamData(
            app_name="v1",
            model_name="LearnPage",
            field_name="content",
            operations_and_block_paths=[
                (SPAN_OPERATION, "full_width_text.content"),
                (SPAN_OPERATION, "expandable_group.body"),
                (SPAN_OPERATION, "well.content"),
            ],
        ),
        MigrateStreamData(
            app_name="v1",
            model_name="DocumentDetailPage",
            field_name="content",
            operations_and_block_paths=[
                (SPAN_OPERATION, "full_width_text.content"),
            ],
        ),
        MigrateStreamData(
            app_name="v1",
            model_name="BlogPage",
            field_name="content",
            operations_and_block_paths=[
                (SPAN_OPERATION, "full_width_text.content"),
            ],
        ),
        MigrateStreamData(
            app_name="v1",
            model_name="LegacyBlogPage",
            field_name="content",
            operations_and_block_paths=[
                (SPAN_OPERATION, "full_width_text.content"),
            ],
        ),
        MigrateStreamData(
            app_name="v1",
            model_name="NewsroomPage",
            field_name="content",
            operations_and_block_paths=[
                (SPAN_OPERATION, "full_width_text.content"),
            ],
        ),
        MigrateStreamData(
            app_name="v1",
            model_name="LegacyNewsroomPage",
            field_name="content",
            operations_and_block_paths=[
                (SPAN_OPERATION, "full_width_text.content"),
            ],
        ),
        MigrateStreamData(
            app_name="v1",
            model_name="BrowsePage",
            field_name="content",
            operations_and_block_paths=[
                (SPAN_OPERATION, "full_width_text.content"),
                # (SPAN_OPERATION, "full_width_text.content_with_anchor"),
                # (SPAN_CLOSE_OPERATION, "full_width_text.content_with_anchor"),
                (SPAN_OPERATION, "expandable_group.body"),
                (SPAN_OPERATION, "well.content"),
                (SPAN_OPERATION, "info_unit_group.intro"),
            ],
        ),
        MigrateStreamData(
            app_name="v1",
            model_name="SublandingPage",
            field_name="content",
            operations_and_block_paths=[
                (SPAN_OPERATION, "full_width_text.content"),
                (SPAN_OPERATION, "expandable_group.body"),
            ],
        ),
    ]
