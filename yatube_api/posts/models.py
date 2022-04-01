import textwrap

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import TextField

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = TextField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.slug


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True
    )

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return (
            f'{textwrap.shorten(self.text, width=15)}, '
            f'{self.pub_date}, '
            f'{self.author.username}, '
            f'{self.group}'
        )


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return (
            f'{textwrap.shorten(self.text, width=15)}, '
            f'{self.post.id}'
            f'{self.created}, '
            f'{self.author.username}'
        )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        models.UniqueConstraint(
            fields=['user', 'following'],
            name='unique follow'
        )
        ordering = ('user', 'following')

    def __str__(self):
        return (
            f'user: {self.user.username}, '
            f'following: {self.following.username}, '
        )
