from django import forms
from .models import Post

# Postモデル用のフォームを作成
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)  # author や published_date は自動設定
