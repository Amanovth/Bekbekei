from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from datetime import datetime


class Stories(models.Model):
    created_at = models.DateTimeField(_("Дата и время"), auto_now_add=True)
    img = models.ImageField(_("Изображение"), upload_to="story_images")
    link = models.URLField(_('Ссылка'), max_length=500, blank=True, null=True, help_text='Если есть')

    class Meta:
        verbose_name = _("История")
        verbose_name_plural = _("Истории")


class StoryVideos(models.Model):
    story = models.ForeignKey(Stories, on_delete=models.CASCADE, related_name="stories")
    url = models.FileField(_("История"), upload_to="stories")
    created_at = models.DateTimeField(_("Дата и время"), auto_now_add=True)

    class Meta:
        verbose_name = _("История")
        verbose_name_plural = _("Истории")

    def __str__(self):
        return self.created_at.strftime("%d %B %Y г. %H:%M")


class Cards(models.Model):
    TYPE_CHOICES = [
        (1, 'Успей купить'),
        (2, 'Специальные предложения')
    ]

    type = models.IntegerField('Тип', choices=TYPE_CHOICES)
    text = models.TextField('Описание', blank=True, null=True)
    title = models.CharField('Название', max_length=150, help_text='Успей купить!')
    datefrom = models.DateField('Дата начала акции')
    dateto = models.DateField('Дата окончания акции')
    date = models.CharField(blank=True, null=True, max_length=150, editable=False)
    img = models.ImageField('Картинка', upload_to='promotions/%Y_%m')

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки (Акция/Предложения)'

    def __str__(self):
        return self.title

    def delete(self):
        if int(self.dateto.strftime('%d')) < int(datetime.today().strftime("%d")):
            if int(self.dateto.strftime('%m')) == int(datetime.today().strftime("%m")):
                self.delete()



class Versions(models.Model):
    version = models.CharField(_("Версия"), max_length=255)
    appstore = models.URLField(_("App Store"))
    googleplay = models.URLField(_("Google Play"))
    date = models.DateTimeField(_("Дата"), auto_now_add=True)
    
    class Meta:
        verbose_name = _("Версия приложения")
        verbose_name_plural = _("Версии приложения")
        
    def __str__(self) -> str:
        return self.version