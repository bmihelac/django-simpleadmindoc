from django.db import models


class Publication(models.Model):
    title = models.CharField(verbose_name='Publication title', max_length=30)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        

class Article(models.Model):
    headline = models.CharField(verbose_name='Article headline', max_length=100, help_text='Headline will be shown in listing page')
    publications = models.ManyToManyField(Publication, verbose_name='In publications')

    def __unicode__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        