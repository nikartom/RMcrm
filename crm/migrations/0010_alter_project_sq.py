# Generated by Django 4.1.5 on 2023-01-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_alter_projectdetail_ads_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sq',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Общая площадь'),
        ),
    ]