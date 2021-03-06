# Generated by Django 2.2.18 on 2021-03-29 22:17
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0049_fix_help_text_typo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='link',
            field=models.URLField(help_text="URL of your landing page. This may contain UTM parameters so you know the traffic came from us. The publisher will be added in the 'ea-publisher' query parameter.", max_length=255, verbose_name='Link URL'),
        ),
    ]
