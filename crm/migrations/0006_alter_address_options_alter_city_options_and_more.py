# Generated by Django 4.1.5 on 2023-01-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_project_accept_alter_project_afz_send_man_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='projectdetail',
            options={'verbose_name': 'Сведенья', 'verbose_name_plural': 'Сведенья'},
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='img',
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='parking_material',
            field=models.CharField(choices=[('1', 'Земля'), ('2', 'Щебень'), ('3', 'Асфальт'), ('4', 'Плитка')], default='3', max_length=128, verbose_name='Покрытие парковки'),
        ),
    ]
