from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_noop
from django.utils.translation import ugettext 

from django.contrib.auth.models import User

# Create your models here.


#-----------------------------------------------------------------
# подписанные пользователи
class ReadUser(models.Model):
    class Meta:
        unique_together = ("user", "signuser")
        index_together  = ["user", "signuser"]
        verbose_name = _('блог пользователя')
        verbose_name_plural = _('1. Блоги пользователей')

    user = models.CharField(
        max_length = 30, 
        editable=False,
        help_text=_('формируется автоматически'),
        verbose_name=_('пользователь'),)
    signuser = models.ForeignKey(User, 
        on_delete=models.CASCADE, 
        verbose_name=_('подписанный пользователь'),)
    
    #---------------------------------------------
    def __str__(self):
        #a = self.user
        a = self.signuser.__str__()       
        return (
            a
            #+ ", " + b
            )


#-----------------------------------------------------------------
# посты в блоге
class BlogPost(models.Model):
    class Meta:
        index_together  = ["user"]
        verbose_name = _('пост блога')
        verbose_name_plural = _('2. Посты блога')

    user = models.CharField(
        max_length = 30, 
        #editable=False,
        help_text=_('формируется автоматически'),
        verbose_name=_('пользователь'),)
    header = models.TextField(
        verbose_name=_('заголовок_'),)
    content = models.TextField(
        verbose_name=_('содержание'),)
    qdate = models.DateTimeField(
        auto_now=True, 
        verbose_name=_('дата создания'),)

    #---------------------------------------------
    def get_absolute_url(self):
        a = "/post/%i/" % self.id
        return a

    #---------------------------------------------
    def __str__(self):
        #a = self.user
        a = self.user
        b = self.header       
        return (
            a
            + ", " + b
            #+ ", " + c
            )


#-----------------------------------------------------------------
# прочитанные посты
class ReadPost(models.Model):
    class Meta:
        unique_together = ("user", "post")
        index_together  = ["user", "post"]
        verbose_name = _('Прочитанный пост')
        verbose_name_plural = _('3. Прочитанные посты')

    user = models.CharField(
        max_length = 30, 
        editable=False,
        help_text=_('формируется автоматически'),
        verbose_name=_('пользователь'),)
    post = models.ForeignKey(BlogPost, 
        on_delete=models.CASCADE, 
        verbose_name=_('прочитанный пост'),)

    #---------------------------------------------
    def __str__(self):
        #a = self.user
        a = self.user
        b = self.post.__str__()       
        return (
            a
            + ", " + b
            #+ ", " + c
            )


