# Generated by Django 3.2.5 on 2021-08-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_listing_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='post_date',
            field=models.DateField(default='2021-08-02'),
        ),
    ]
