# Generated by Django 3.1.3 on 2020-12-18 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0017_transactions_source_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='source_game',
            new_name='source',
        ),
    ]
