# Generated by Django 4.2.4 on 2023-09-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompoundWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound_words', models.TextField(blank=True, null=True, verbose_name='Кошмок сөздөр')),
            ],
            options={
                'verbose_name': 'Кошмок сөздөр',
                'verbose_name_plural': 'Кошмок сөздөр',
            },
        ),
        migrations.CreateModel(
            name='kgText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='Класс')),
                ('book_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Чыгарманын аты')),
                ('book_author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автору')),
                ('book_text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('words_q', models.IntegerField(blank=True, null=True, verbose_name='Сөздөрдүн саны')),
                ('syllables_avg', models.FloatField(blank=True, null=True, verbose_name='Сөздөрдүн орточо узундугу муундар менен')),
                ('sentence_q', models.IntegerField(blank=True, null=True, verbose_name='Сүйлөмдөрдүн жалпы саны')),
                ('sentence_avg', models.FloatField(blank=True, null=True, verbose_name='Сүйлөмдүрдүн орточо узундугу сөздөр менен')),
                ('multisyllabic_wq', models.FloatField(blank=True, null=True, verbose_name='Көп муунду сөздөрдүн саны')),
                ('compound_w_q', models.FloatField(blank=True, null=True, verbose_name='Татаал жана кош сөздөрдүн саны')),
                ('rareword_q', models.FloatField(blank=True, null=True, verbose_name='Сейрек сөздөрдүн саны')),
                ('rareword_p', models.FloatField(blank=True, null=True, verbose_name='Сейрек сөздөрдүн %')),
                ('complex_w_q', models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны')),
                ('all_compound_words_p', models.FloatField(blank=True, null=True, verbose_name='Татаал сөздөрдүн % ')),
                ('fw_q', models.FloatField(blank=True, null=True, verbose_name='Көп колдонулган сөздөр')),
                ('fw_p', models.FloatField(blank=True, null=True, verbose_name='Көп колдонулган сөздөрдүн %')),
                ('uniq_w', models.IntegerField(blank=True, null=True, verbose_name='Уникалдуу сөздөрдүн саны')),
                ('lexical_div', models.FloatField(blank=True, null=True, verbose_name='Коэф. лекс-го разн-ия')),
                ('level_result', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сунушталган класс')),
            ],
            options={
                'verbose_name': 'Кыргызча текст',
                'verbose_name_plural': 'Кыргызча тексттер',
            },
        ),
        migrations.DeleteModel(
            name='uzText',
        ),
        migrations.AlterModelOptions(
            name='freqword',
            options={'verbose_name': 'Көп колдонулган сөздөр', 'verbose_name_plural': 'Көп колдонулган сөздөр'},
        ),
        migrations.AlterModelOptions(
            name='lcword',
            options={'verbose_name': 'Татаал сөздөр', 'verbose_name_plural': 'Татаал сөздөр'},
        ),
        migrations.AlterModelOptions(
            name='rareword',
            options={'verbose_name': 'Сейрек сөздөр', 'verbose_name_plural': 'Сейрек сөздөр'},
        ),
        migrations.RenameField(
            model_name='g1level',
            old_name='g1_longw_q_l1',
            new_name='g1_multisyllabic_wq_l1',
        ),
        migrations.RenameField(
            model_name='g1level',
            old_name='g1_longw_q_l2',
            new_name='g1_multisyllabic_wq_l2',
        ),
        migrations.RenameField(
            model_name='g1level',
            old_name='g1_longw_q_l3',
            new_name='g1_multisyllabic_wq_l3',
        ),
        migrations.RenameField(
            model_name='g2level',
            old_name='g2_longw_q_l1',
            new_name='g2_multisyllabic_wq_l1',
        ),
        migrations.RenameField(
            model_name='g2level',
            old_name='g2_longw_q_l2',
            new_name='g2_multisyllabic_wq_l2',
        ),
        migrations.RenameField(
            model_name='g3level',
            old_name='g3_longw_q_l1',
            new_name='g3_multisyllabic_wq_l1',
        ),
        migrations.RenameField(
            model_name='g3level',
            old_name='g3_longw_q_l2',
            new_name='g3_multisyllabic_wq_l2',
        ),
        migrations.RenameField(
            model_name='g4level',
            old_name='g4_longw_q_l1',
            new_name='g4_multisyllabic_wq_l1',
        ),
        migrations.RenameField(
            model_name='g4level',
            old_name='g4_longw_q_l2',
            new_name='g4_multisyllabic_wq_l2',
        ),
        migrations.AddField(
            model_name='g1level',
            name='g1_complexw_q_l1',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 1.1'),
        ),
        migrations.AddField(
            model_name='g1level',
            name='g1_complexw_q_l2',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 1.2'),
        ),
        migrations.AddField(
            model_name='g1level',
            name='g1_complexw_q_l3',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 1.3'),
        ),
        migrations.AddField(
            model_name='g2level',
            name='g2_complexw_q_l1',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 2.1'),
        ),
        migrations.AddField(
            model_name='g2level',
            name='g2_complexw_q_l2',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 2.2'),
        ),
        migrations.AddField(
            model_name='g3level',
            name='g3_complexw_q_l1',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 3.1'),
        ),
        migrations.AddField(
            model_name='g3level',
            name='g3_complexw_q_l2',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 3.2'),
        ),
        migrations.AddField(
            model_name='g4level',
            name='g4_complexw_q_l1',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 4.1'),
        ),
        migrations.AddField(
            model_name='g4level',
            name='g4_complexw_q_l2',
            field=models.FloatField(blank=True, null=True, verbose_name='Кошмок сөздөрдүн саны 4.2'),
        ),
        migrations.AlterField(
            model_name='freqword',
            name='freq_words',
            field=models.TextField(blank=True, null=True, verbose_name='Көп колдонулган сөздөр'),
        ),
        migrations.AlterField(
            model_name='lcword',
            name='lc_words',
            field=models.TextField(blank=True, null=True, verbose_name='Татаал сөздөр'),
        ),
        migrations.AlterField(
            model_name='rareword',
            name='rare_words',
            field=models.TextField(blank=True, null=True, verbose_name='Сейрек сөздөр'),
        ),
    ]
