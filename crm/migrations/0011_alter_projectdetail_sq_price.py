# Generated by Django 4.1.5 on 2023-01-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_alter_project_sq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='sq_price',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Цена за квадрат'),
        ),
    ]