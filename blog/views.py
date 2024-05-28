from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ('name', 'description', 'image', 'created_at', 'publication')
    success_url = reverse_lazy('blog:list')


    def form_valid(self, form):
        if form.is_valid():
            new_artucle = form.save()
            new_artucle.slug = slugify(new_artucle.name)
            new_artucle.save()
            return super().form_valid(form)



class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.caunt_views +=1
        self.object.save()
        return self.object


class ArticleUpdatelView(UpdateView):
    model = Article
    fields = ('name', 'description', 'image', 'created_at', 'publication')

    def form_valid(self, form):
        if form.is_valid():
            new_artucle = form.save()
            new_artucle.slug = slugify(new_artucle.name)
            new_artucle.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:list')