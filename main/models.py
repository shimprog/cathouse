from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Materialimodel(models.Model):
    name = models.CharField('Имя материала', max_length=50)
    cvetmateriala = models.CharField('Цвет материала', max_length=11)
    visotavorsa = models.CharField('Высота ворса', max_length=11)
    opisanie = RichTextUploadingField()
    imagenews = models.ImageField("Изображение", upload_to="material/", default='')
    url = models.SlugField(max_length=130, null=True, blank=True, default='')

    def get_absolute_url(self):
        return reverse("materialfull", kwargs={"slug": self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'




class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    housenumber = models.CharField('Дом №', max_length=10, default=None)
    cenaot = models.CharField('Цена от', max_length=15, default='')
    minopisanie = models.TextField('Короткое описание', default=None)
    opisanie = models.TextField('Описание')
    model_house = models.FileField("Файл модели", upload_to="gltf/", null=True, blank=True)
    poster = models.ImageField("Изображение", upload_to="poster/")
    treemodel = models.TextField("Код модели")
    typedoma = models.CharField('Тип дома', max_length=5, null=True, blank=True, default='')
    url = models.SlugField(max_length=130, unique=True)


    def get_absolute_url(self):
        return reverse("productfull", kwargs={"slug": self.url})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукцию'
        verbose_name_plural = 'Продукция'


class News(models.Model):
    title = models.CharField('Название', max_length=250)
    poster = models.ImageField("Постер", upload_to="poster/", default='')
    miniopisanie = models.TextField('Мини описание', null=True, blank=True, default='')
    opisanie = RichTextUploadingField()
    datapublic = models.DateField("Дата публикации")
    imagenews = models.ImageField("Изображение", upload_to="poster/", default='')
    url = models.SlugField(max_length=130, unique=True)

    def get_absolute_url(self):
        return reverse("newsfull", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Obratnaya(models.Model):
    name = models.CharField('Имя покупателя', max_length=50)
    telefon = models.CharField('Телефон', max_length=12)
    opisanie = models.TextField('Описание')
    temaobrash = models.CharField('Тема', max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return self.name+' '+self.telefon

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'


class Svoyamodel(models.Model):
    name = models.CharField('Имя покупателя', max_length=50)
    telefon = models.CharField('Телефон', max_length=12)
    opisanie = models.TextField('Описание')
    chertej = models.ImageField('Чертеж модели', upload_to="zakazi/")
    shirina = models.CharField('Ширина', max_length=12, null=True, blank=True)
    visota = models.CharField('Высота', max_length=12, null=True, blank=True)
    glubina = models.CharField('Глубина', max_length=12, null=True, blank=True)


    def __str__(self):
        return self.name+' '+self.telefon

    class Meta:
        verbose_name = 'Заказ по своей модели'
        verbose_name_plural = 'Заказы по своей модели'


class Zakazmodel(models.Model):
    name = models.CharField('Имя покупателя', max_length=50)
    telefon = models.CharField('Телефон', max_length=12)
    shirina = models.CharField('Ширина', max_length=12, null=True, blank=True)
    visota = models.CharField('Высота', max_length=12, null=True, blank=True)
    glubina = models.CharField('Глубина', max_length=12, null=True, blank=True)
    name_house = models.CharField('Название', max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name+' '+self.telefon

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'