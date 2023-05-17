from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView

# Create your views here.

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'


class NewsDelailView(DetailView):
    model = News
    template_name = 'news_detial.html'