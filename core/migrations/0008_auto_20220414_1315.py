# Generated by Django 3.1.4 on 2022-04-14 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220414_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance',
            old_name='product_insurance',
            new_name='product',
        ),
    ]