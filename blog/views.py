# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post  # Postモデルをインポート
from django.utils import timezone  # 時刻操作用

# ブログ記事一覧ページ
def post_list(request):
    # 公開日が現在時刻以下の記事を取得して日付順に並べる
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # post_list.html テンプレートに posts を渡してレンダリング
    return render(request, 'blog/post_list.html', {'posts': posts})

# ブログ記事詳細ページ
def post_detail(request, pk):
    # プライマリキー(pk)に一致する記事を取得。存在しない場合は404ページ
    post = get_object_or_404(Post, pk=pk)
    # post_detail.html テンプレートに post を渡してレンダリング
    return render(request, 'blog/post_detail.html', {'post': post})
