from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='title', max_length=50)
    text = models.TextField(verbose_name='正文', max_length=10000)
    pub_date = models.DateTimeField(verbose_name='date published')
    last_modified = models.DateTimeField(verbose_name='最近修改时间', auto_now=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.title
