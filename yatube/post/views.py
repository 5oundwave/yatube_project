from django.shortcuts import render, get_object_or_404

from posts.models import Post, Group

# Главная страница
def index(request):
    template = 'posts/index.html'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, template, context)

# View-функция для страницы сообщества:
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_posts.html'
    title = 'Посты'
    posts = Post.objects.all()
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context,)