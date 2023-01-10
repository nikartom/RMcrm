# Generated by Django 4.1.5 on 2023-01-09 09:49

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('region_field', models.CharField(choices=[('22', 'Алтайский край'), ('28', 'Амурская область'), ('29', 'Архангельская область'), ('30', 'Астраханская область'), ('31', 'Белгородская область'), ('32', 'Брянская область'), ('33', 'Владимирская область'), ('34', 'Волгоградская область'), ('35', 'Вологодская область'), ('36', 'Воронежская область'), ('77', 'город федерального значения Москва'), ('78', 'город федерального значения Санкт-Петербург'), ('92', 'город федерального значения Севастополь'), ('93', 'Донецкая Народная Республика'), ('79', 'Еврейская автономная область'), ('75', 'Забайкальский край'), ('90', 'Запорожская область'), ('37', 'Ивановская область'), ('99', 'Иные территории,включая город и космодром Байконур'), ('38', 'Иркутская область'), ('7', 'Кабардино-Балкарская Республика'), ('39', 'Калининградская область'), ('40', 'Калужская область'), ('41', 'Камчатский край'), ('9', 'Карачаево-Черкесская Республика'), ('42', 'Кемеровская область — Кузбасс'), ('43', 'Кировская область'), ('44', 'Костромская область'), ('23', 'Краснодарский край'), ('24', 'Красноярский край'), ('45', 'Курганская область'), ('46', 'Курская область'), ('47', 'Ленинградская область'), ('48', 'Липецкая область'), ('94', 'Луганская Народная Республика'), ('49', 'Магаданская область'), ('50', 'Московская область'), ('51', 'Мурманская область'), ('83', 'Ненецкий автономный округ'), ('52', 'Нижегородская область'), ('53', 'Новгородская область'), ('54', 'Новосибирская область'), ('55', 'Омская область'), ('56', 'Оренбургская область'), ('57', 'Орловская область'), ('58', 'Пензенская область'), ('59', 'Пермский край'), ('25', 'Приморский край'), ('60', 'Псковская область'), ('1', 'Республика Адыгея (Адыгея)'), ('4', 'Республика Алтай'), ('2', 'Республика Башкортостан'), ('3', 'Республика Бурятия'), ('5', 'Республика Дагестан'), ('6', 'Республика Ингушетия'), ('8', 'Республика Калмыкия'), ('10', 'Республика Карелия'), ('11', 'Республика Коми'), ('91', 'Республика Крым'), ('12', 'Республика Марий Эл'), ('13', 'Республика Мордовия'), ('14', 'Республика Саха (Якутия)'), ('15', 'Республика Северная Осетия — Алания'), ('16', 'Республика Татарстан (Татарстан)'), ('17', 'Республика Тыва'), ('19', 'Республика Хакасия'), ('61', 'Ростовская область'), ('62', 'Рязанская область'), ('63', 'Самарская область'), ('64', 'Саратовская область'), ('65', 'Сахалинская область'), ('66', 'Свердловская область'), ('67', 'Смоленская область'), ('26', 'Ставропольский край'), ('68', 'Тамбовская область'), ('69', 'Тверская область'), ('70', 'Томская область'), ('71', 'Тульская область'), ('72', 'Тюменская область'), ('18', 'Удмуртская Республика'), ('73', 'Ульяновская область'), ('27', 'Хабаровский край'), ('86', 'Ханты-Мансийский автономный округ — Югра'), ('95', 'Херсонская область'), ('74', 'Челябинская область'), ('20', 'Чеченская Республика'), ('21', 'Чувашская Республика — Чувашия'), ('87', 'Чукотский автономный округ'), ('89', 'Ямало-Ненецкий автономный округ'), ('76', 'Ярославская область')], default='23', max_length=256)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
