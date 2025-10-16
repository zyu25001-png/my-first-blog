from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),       # 博客首页
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # 博文详情页
    path('post/new/', views.post_new, name='post_new'),  # 新建博文
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # 编辑博文
]
