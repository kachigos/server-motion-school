from operator import mod
from re import T
from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=100)
    file = models.FileField(verbose_name='Файл', upload_to='file/category')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Chronology(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    pub_date = models.DateField(verbose_name='Дата')
    participants = models.CharField(verbose_name='Участники', max_length=100)
    organizer = models.CharField(verbose_name='Организатор', max_length=50)
    description = models.TextField(verbose_name='Вверхние описание')
    description_info = models.TextField(verbose_name='Нижнее описание', blank=True)
    url_video = models.URLField(verbose_name='Добавление ссылок на видео', max_length=200, blank=True, null=True)
    image = models.ImageField(verbose_name='Фото', upload_to='Хронология/', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Хронология'
        verbose_name_plural = 'Хронология'
    
    def save(self, *args, **kwargs):
        if not self.url_video and not self.image:
            raise ValueError('Хотя бы один заполни!')
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Administration(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='Administration/')
    fullname = models.CharField(verbose_name='Ф.И.О', max_length=100)
    lesson = models.CharField(verbose_name='Предмет', max_length=50)
    position = models.CharField(verbose_name='Должность', max_length=50)

    def __str__(self) -> str:
        return self.fullname


    class Meta:
            verbose_name = 'Администрация'
            verbose_name_plural = 'Администрация'


class Accreditation(models.Model):
    PARENT_ACCRE = (
        ('Институционалдык', 'Институционалдык'),
        ('Программалык', 'Программалык'),
    )
    which_accred = models.CharField(max_length=20, choices=PARENT_ACCRE, verbose_name='Аккредитация')
    name = models.CharField(verbose_name='Название события', max_length=100)
    files = models.ManyToManyField('File', verbose_name='Файлы', null=True, blank=True)

    class Meta:
        verbose_name = 'Аккредитация'
        verbose_name_plural = 'Аккредитации'

    def __str__(self):
        return self.name


class File(models.Model):
    name_file = models.CharField(verbose_name='Название файла', max_length=64)
    file = models.FileField(verbose_name='Подпункты (ссылка на док)необязательное поле', upload_to='file/accreditation')

    def __str__(self) -> str:
        return self.name_file

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Teacher(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='Teachers/')
    full_name = models.CharField(verbose_name='Ф.И.О', max_length=64)
    lesson = models.CharField(verbose_name='Предмет', max_length=100)
    experience = models.CharField(verbose_name='Стаж', max_length=100)
    show_main_page = models.BooleanField(verbose_name='Показать на главной странице', default=False)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.full_name


