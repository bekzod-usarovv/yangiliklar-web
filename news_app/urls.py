from django.urls import path
from.views import NewsListView, NewsDelailView

urlpatterns =[
    path('all/',NewsListView.as_view(), name='news_list'),
    path('all/<int:pk>/',NewsDelailView.as_view(), name='news_detail')
]