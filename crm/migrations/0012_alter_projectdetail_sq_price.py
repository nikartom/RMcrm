# Generated by Django 4.1.5 on 2023-01-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_alter_projectdetail_sq_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='sq_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Цена за квадрат'),
        ),
    ]
