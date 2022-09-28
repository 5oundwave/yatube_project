# posts/views.py
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post,Group

def index_list(request):
    template = 'posts/index.html'
    title = 'Главная страница проекта'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)

# View-функция для страницы сообщества:
def group_posts_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_posts.html'
    title = 'Все записи'
    posts = Post.objects.all()
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context,)