# Generated by Django 3.2.18 on 2023-04-12 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0003_auto_20230410_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordhistoryitem',
            name='expires_at',
        ),
        migrations.RemoveField(
            model_name='passwordhistoryitem',
            name='locked_until',
        ),
        migrations.AlterField(
            model_name='passwordhistoryitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_history', to=settings.AUTH_USER_MODEL),
        ),
    ]
