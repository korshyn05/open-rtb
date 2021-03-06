# Generated by Django 2.2.26 on 2022-02-04 16:33
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0008_2_5'),
        ('adserver', '0064_data_stripe_fk_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='invoices',
            field=models.ManyToManyField(blank=True, to='djstripe.Invoice', verbose_name='Stripe invoices'),
        ),
    ]
