from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from profiles.models import UserNet
from comments.models import AbstractComment


class Post(models.Model):
    text = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    times_viewed = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(UserNet, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_edited:
            return f"{self.author}: {self.text[:25]} EDITED AT {self.edited_at}"
        return f"{self.author}: {self.text[:25]} {self.created_at}"

    def comments_count(self):
        return self.comments.count()


class Comment(AbstractComment, MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserNet, on_delete=models.SET_NULL, null=True)
    parent = TreeForeignKey('self',
                            verbose_name='Parent comment',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children')

    def __str__(self):
        if self.is_edited:
            return f"TO {self.post} => {self.author}: {self.text[:25]} EDITED AT {self.edited_at}"
        return f"{self.author}: {self.text[:25]} {self.created_at}"