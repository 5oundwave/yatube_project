from django.urls import path,include

app_name = 'url'

urlpatterns = [
    path('', include(('posts.urls', 'index_list'), namespace = 'index')),

    path('group/<slug:slug>/', include(('posts.urls', 'posts_list'), namespace='group_posts')),
]