from django.shortcuts import render
from .models import Blog
from django.urls import reverse
from django.http import HttpResponseRedirect


# Главная страница, на которой отображается 10 последних опубликованных постов от свежих к старым.
# У каждого поста, помимо названия и текста, должны отображаться иллюстрация и  дата публикации.
# В шапке страницы должна отображаться самая свежая статья.
MAX_ARTICLE_NUM = 10


def homepage(request):
    articles = Blog.objects.order_by('-publication_date')
    print(articles)
    print(Blog.objects.all())
    article_num = len(articles)
    if article_num == 0:
        context = {}
    else:
        newest_article = articles[0]
        articles = articles[1:] if article_num < MAX_ARTICLE_NUM else articles[1:MAX_ARTICLE_NUM]
        context = {
            "articles": articles,
            "newest_article": newest_article,
        }
    return render(request, "main/index.html", context)


# Страница для добавления поста с формой,
# содержащей поле для названия поста,
# поле для текста поста и поле для загрузки иллюстрации к посту.
# Здесь пользователь может писать и публиковать свои посты.
def add_article(request):
    if request.method == "POST":
        title = request.POST["title"]
        article_text = request.POST["article_text"]
        image = request.FILES['image']
        # subheading = request.POST["subheading"]
        # summary = request.POST["summary"]
        if len(article_text) == 0 or len(title) == 0 or image is None:
            return render(request, "main/write_article.html",
                          {
                              "error_msg": "You did not provide article text.",
                          })
        else:
            Blog.objects.create(title=title, text=article_text, image=image)
            return HttpResponseRedirect(reverse('main:homepage'))
    context = {}
    return render(request, "main/write_article.html", context)


# Страница, на которой можно прочитать полный текст статьи
# (чтобы перейти на нее, нужно кликнуть на кнопку "Читать" для статьи, находящейся в шапке,
# либо на плитку статьи - для всех остальных статей).
def ith_article(request, article_id):
    article = Blog.objects.filter(pk=article_id)[0]
    context = {
        "article": article,
    }
    print(article)
    return render(request, "main/view_article.html", context)
