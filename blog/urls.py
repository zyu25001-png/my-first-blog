from django.urls import path
from . import views

# URLパターンのリスト
urlpatterns = [
    # ホームページ：記事一覧
    path('', views.post_list, name='post_list'),

    # 記事詳細ページ。pkはプライマリキー
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
