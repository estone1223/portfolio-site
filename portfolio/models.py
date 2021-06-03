from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.


class ProfileModel(models.Model):
    name = models.CharField('名前', max_length=100)
    image = models.ImageField('イメージ', upload_to='profile')
    career = models.CharField('職業', max_length=55, null=True, blank=True)
    age = models.IntegerField('年齢', null=True, blank=True)
    org = models.CharField('所属組織', max_length=100, null=True, blank=True)
    twitter = models.URLField('TwitterのURL', null=True, blank=True)
    introduction = models.TextField('自己紹介文')

    def __str__(self):
        display_name = self.name
        return display_name

    class Meta:
        verbose_name_plural = 'プロフィール'


class DescriptionModel(models.Model):
    text = models.TextField('本文', max_length=255)

    def __str__(self):
        display_name = self.text
        return display_name

    class Meta:
        verbose_name_plural = 'スキルの概要文'


class SkillModel(models.Model):
    name = models.CharField('名前', max_length=100)
    years = models.IntegerField('経験年数', default=0)
    description = models.ForeignKey(
        DescriptionModel, on_delete=SET_NULL, null=True)

    def __str__(self):
        display_name = self.name
        return display_name

    class Meta:
        verbose_name_plural = 'スキル'


class WorkModel(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField('イメージ', upload_to='works', null=True, blank=True)
    url = models.URLField('URL', null=True)
    published = models.DateField('公開日', null=True, blank=True)

    def __str__(self):
        display_name = self.title
        return display_name

    class Meta:
        verbose_name_plural = '作品'
