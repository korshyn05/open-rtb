# Generated by Django 2.2.24 on 2022-01-14 23:38
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0008_2_5'),
        ('adserver', '0062_add_saas_attribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertiser',
            name='djstripe_customer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.Customer', verbose_name='Stripe Customer'),
        ),
        migrations.AddField(
            model_name='historicaladvertiser',
            name='djstripe_customer',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='djstripe.Customer', verbose_name='Stripe Customer'),
        ),
        migrations.AddField(
            model_name='historicalpublisher',
            name='djstripe_account',
            field=models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='djstripe.Account', verbose_name='Stripe connected account'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='djstripe_account',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.Account', verbose_name='Stripe connected account'),
        ),
    ]
