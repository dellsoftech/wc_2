# Generated by Django 4.2.4 on 2023-10-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uz', '0007_alter_g1level_options_alter_g2level_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uztext',
            name='fw_p',
            field=models.FloatField(blank=True, null=True, verbose_name='% Часто используемых слов'),
        ),
    ]