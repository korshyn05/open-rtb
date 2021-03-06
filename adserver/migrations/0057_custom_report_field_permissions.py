# Generated by Django 2.2.24 on 2021-07-22 15:43
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adserver', '0056_publishergroup_specific_adtypes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertiser',
            options={'ordering': ('name',), 'permissions': [('staff_advertiser_fields', 'Can view staff advertiser fields in reports')]},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ('name',), 'permissions': [('staff_publisher_fields', 'Can view staff publisher fields in reports')]},
        ),
    ]
