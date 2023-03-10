from django.db import models
from django.utils import timezone

from accounts.items import REGIONS
from accounts.models import User

MFCLIST = [
    ("1", "МФЦ"),
    ("2", "ЭЦП"),
]

MATERIAL = [
    ("1", "Бетон"),
    ("2", "Плитка"),
    ("3", "Дерево"),
    ("4", "Металл"),
    ("5", "Гипсокартон"),
]

SEWER = [
    ("1", "Центральня"),
    ("2", "Септик"),
    ("3", "Сололифт"),
    ("4", "Отсутствует"),
]

WATER = [
    ("cold", "Холодная вода"),
    ("warm", "Холодная и горячая вода"),
    ("none", "Без водоснабжения"),
]


HEAT = [
    ("1", "Центральное"),
    ("2", "Газ"),
    ("3", "Печное"),
    ("4", "Электрокотел"),
    ("5", "Другое"),
]

PARKING = [
    ("1", "Земля"),
    ("2", "Щебень"),
    ("3", "Асфальт"),
    ("4", "Плитка"),
]


class City(models.Model):
    obl = models.CharField(max_length=255, choices=REGIONS, default="24", verbose_name="Регион")
    name = models.CharField(max_length=128, verbose_name="Город")
    population = models.IntegerField()

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    numb = models.CharField(max_length=64, verbose_name="Номер дома")

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f"{self.street}, {self.numb}"


class Project(models.Model):
    manager = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Сотрудник")
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name="Адрес")
    file = models.URLField(verbose_name="Ссылка на презентацию")
    sq = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Общая площадь")
    rent_tax = models.PositiveIntegerField(verbose_name="Арендная ставка")
    act_reg = models.BooleanField(default=False, verbose_name="Регистрация с актом/без")
    mfc = models.CharField(max_length=10, choices=MFCLIST, verbose_name="ЭЦП/МФЦ", blank=True)
    vis = models.DateField(verbose_name="Подписан дата", blank=True, null=True)
    accept = models.DateField(verbose_name="Принят дата", blank=True, null=True)
    app_send_man = models.DateField(verbose_name="АПП отдал менеджеру", blank=True, null=True)
    app_send_sopr = models.DateField(verbose_name="АПП отдал сопроводителю", blank=True, null=True)
    afz_send_man = models.DateField(verbose_name="АФЗ отдал менеджеру", blank=True, null=True)
    afz_send_sopr = models.DateField(verbose_name="АФЗ отдал сопроводителю", blank=True, null=True)
    vis_buid = models.DateField(verbose_name="Стройка подписана", blank=True, null=True)
    answer = models.TextField(verbose_name="Ответ", blank=True)
    comment = models.TextField(verbose_name="Комментарий", blank=True)
    vis_bool = models.BooleanField(default=False, verbose_name="Подписан")
    approve = models.BooleanField(default=False, verbose_name="Принят")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return str(self.address)


class ProjectDetail(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, verbose_name="Проект")
    # img = models.ImageField(upload_to=("1"), verbose_name="Обложка объекта", blank=True)
    lessor = models.CharField(max_length=255, verbose_name="Контактное лицо")
    lessor_phone = models.PositiveBigIntegerField(verbose_name="Телефон")
    sq_bay = models.IntegerField(verbose_name="Торговая площадь")
    sq_basemant = models.IntegerField(verbose_name="Площадь подвала", null=True, blank=True)
    sq_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена за квадрат", null=True, blank=True)
    len_rent = models.SmallIntegerField(verbose_name="Максимальный срок аренды", null=True, blank=True)
    floor_material = models.CharField(max_length=128, choices=MATERIAL, default="2", verbose_name="Материал пола")
    floor_level = models.BooleanField(default=True, verbose_name="Все полы в одном уровне")
    floor_var = models.BooleanField(
        default=True, verbose_name="Одинаковые ли полы в подсобных помещениях и в торговом зале"
    )
    roof_stat = models.BooleanField(default=False, verbose_name="Протечки потолка")
    debarkader = models.BooleanField(default=True, verbose_name="Дебаркадер")
    radius_school = models.BooleanField(
        default=False, verbose_name="Наличие учреждений являющимися запретом для торговли табака, алкоголя"
    )
    radius_len = models.PositiveSmallIntegerField(verbose_name="Расстояние до учереждения", blank=True, null=True)
    radius_bool = models.BooleanField(default=True, verbose_name="Проходит по законодательству")
    sewer = models.CharField(max_length=128, choices=SEWER, default="1", verbose_name="Канализация")
    water = models.CharField(max_length=128, choices=WATER, default="warm", verbose_name="Водоснабжение")
    electric = models.PositiveSmallIntegerField(verbose_name="Электроэнергия, кВт")
    electric_up = models.BooleanField(default=True, verbose_name="Возможность повышения кВт")
    heat = models.CharField(max_length=128, choices=HEAT, default="1", verbose_name="Отопление")
    parking_len = models.PositiveSmallIntegerField(verbose_name="Расстояние от парковки до входа")
    parking_material = models.CharField(max_length=128, choices=PARKING, default="3", verbose_name="Покрытие парковки")
    parking_max = models.PositiveSmallIntegerField(verbose_name="Вместимость парковки")
    delay = models.BooleanField(default=True, verbose_name="Отсрочка")
    delay_len = models.CharField(max_length=255, verbose_name="Длительность отсрочки", blank=True, null=True)
    repair = models.CharField(max_length=255, verbose_name="Ремонт или отсрочка", blank=True, null=True)
    comment = models.TextField(verbose_name="Комментарий сотрудника по объекту(если есть)", blank=True, null=True)
    ads_url = models.URLField(verbose_name="Ссылка на обьявление", blank=True, null=True)
    resume = models.TextField(verbose_name="Резюме SV(Развития)", blank=True, null=True)
    complite = models.BooleanField(default=False, verbose_name="Документ завершен")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сведенья'
        verbose_name_plural = 'Сведенья'

    def __str__(self):
        return str(self.project)
