from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add', views.add_article, name='add_article'),
    path('articles/<int:article_id>', views.ith_article, name='ith_article'),
]
