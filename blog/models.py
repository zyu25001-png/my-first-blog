from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        """承認済みコメントを取得するメソッド"""
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

# コメントモデル - ブログ記事に対するコメントを管理
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')  # 記事との関連付け
    author = models.CharField(max_length=200)  # コメント投稿者名
    text = models.TextField()  # コメント内容
    created_date = models.DateTimeField(default=timezone.now)  # 作成日時
    approved_comment = models.BooleanField(default=False)  # 承認フラグ（デフォルトは未承認）

    def approve(self):
        """コメントを承認するメソッド"""
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text