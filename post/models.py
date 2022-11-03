from django.db import models
from accounts.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=30)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.PositiveSmallIntegerField('LIKE', default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        ordering = ('update_dt',)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content

    class Meta:
        db_table = 'comment'