# Generated by Django 5.0.3 on 2024-04-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_blog_options_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_flag',
            field=models.BooleanField(default=True, verbose_name='Признак текущей версии'),
        ),
    ]
