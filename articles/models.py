from django.db import models
from i18nfield.fields import I18nCharField, I18nTextField

class Article(models.Model):
    title = I18nCharField(verbose_name='Title', max_length=200)

    #author = models.CharField(("Author"), max_length=200)

    def __unicode__(self):
        return self.title