from django import forms
from .models import Post, Comment

# Postモデル用のフォームを作成
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)  # author や published_date は自動設定

# コメント用のフォームを作成
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)  # post と created_date は自動設定
