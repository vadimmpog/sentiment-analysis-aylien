# Generated by Django 4.0.4 on 2022-05-16 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysisapp', '0003_analysis_confidence_analysis_irony_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysis',
            old_name='user_id',
            new_name='user',
        ),
    ]