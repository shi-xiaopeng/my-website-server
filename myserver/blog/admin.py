from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'pub_date', 'last_modified', 'created')
    list_filter = ['pub_date', 'created']
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
