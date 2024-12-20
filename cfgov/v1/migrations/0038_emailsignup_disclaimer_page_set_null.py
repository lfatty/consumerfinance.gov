# Generated by Django 4.2.14 on 2024-08-26 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
        ('v1', '0037_add_table_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsignup',
            name='disclaimer_page',
            field=models.ForeignKey(blank=True, help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.page', verbose_name='Privacy Act statement'),
        ),
    ]
