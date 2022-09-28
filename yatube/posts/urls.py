from django.urls import path

from . import views

app_name = 'group_posts'
app_name = 'index'

urlpatterns = [
    path('', views.index_list, name = 'index_list'),

    path('group/<slug:slug>/', views.group_posts_list, name='group_posts_list'),
]