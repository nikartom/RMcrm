from django.db import models
from accounts.items import REGIONS
from accounts.models import User

MFCLIST = [('1', 'МФЦ'),
    ('2', 'ЭЦП'),]

class City(models.Model):
    obl = models.CharField(max_length=255, choices=REGIONS, default='24', verbose_name="Регион")
    name = models.CharField(max_length=128, verbose_name='Город')

    def __str__(self):
        return self.name

class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    numb = models.CharField(max_length=64, verbose_name='Номер дома')

    def __str__(self):
        return self.street



class Project(models.Model):
    manager = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Сотрудник")
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name="Адрес")
    sq = models.FloatField(verbose_name="Площадь")
    rent_tax = models.PositiveIntegerField(verbose_name="Арендная ставка")
    act_reg = models.BooleanField(default=False, verbose_name="Регистрация с актом/без")
    mfc = models.CharField(max_length=10, choices=MFCLIST, verbose_name="ЭЦП/МФЦ", blank=True)
    vis = models.DateField(verbose_name="Подписан дата", blank=True)
    accept = models.DateField(verbose_name="Принят дата", blank=True)
    app_send_man = models.DateField(verbose_name="АПП отдал менеджеру", blank=True)
    app_send_sopr = models.DateField(verbose_name="АПП отдал сопроводителю", blank=True)
    afz_send_man = models.DateField(verbose_name="АФЗ отдал менеджеру", blank=True)
    afz_send_sopr = models.DateField(verbose_name="АФЗ отдал сопроводителю", blank=True)
    vis_buid = models.DateField(verbose_name="Стройка подписана", blank=True)
    answer = models.TextField(verbose_name="Ответ", blank=True)
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    vis_bool = models.BooleanField(default=False, verbose_name="Подписан")
    approve = models.BooleanField(default=False, verbose_name="Принят")

    def __str__(self):
        return str(self.address)




    
