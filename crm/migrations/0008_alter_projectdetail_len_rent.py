# Generated by Django 4.1.5 on 2023-01-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_alter_projectdetail_delay_len_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='len_rent',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Максимальный срок аренды'),
        ),
    ]
