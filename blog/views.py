from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post, Comment

def post_list(request):
    # 显示所有文章，按创建时间倒序排列
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# コメント追加ビュー
def add_comment_to_post(request, pk):
    """記事にコメントを追加するビュー"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # コメントを記事に関連付け
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

# コメント承認ビュー（ログイン必須）
@login_required
def comment_approve(request, pk):
    """コメントを承認するビュー"""
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog:post_detail', pk=comment.post.pk)

# コメント削除ビュー（ログイン必須）
@login_required
def comment_remove(request, pk):
    """コメントを削除するビュー"""
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:post_detail', pk=comment.post.pk)

# 草稿一覧ビュー（ログイン必須）
@login_required
def post_draft_list(request):
    """草稿の一覧を表示するビュー"""
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

# 記事掲載ビュー（ログイン必須）
@login_required
def post_publish(request, pk):
    """記事を掲載するビュー"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.publish()
    return redirect('blog:post_detail', pk=pk)

# 記事削除ビュー（ログイン必須）
@login_required
def post_remove(request, pk):
    """記事を削除するビュー"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('blog:post_list')
