from django.views import generic
from .models import Article
from django.utils import timezone


class ArticleIndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now())


class ArticleDetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Article
