from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=24,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        verbose_name='название'
    )
    slug = models.SlugField(
        max_length=24,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        # db_table = 'blog_category'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        # ordering = ('-name', )
        # abstract = False
        # app_label = 'blog'
        # managed = False


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        verbose_name='заголовок'
    )
    body = models.TextField(
        null=False,
        blank=False,
        verbose_name='описание'
    )
    date_publish = models.DateTimeField(
        verbose_name='дата публикации',
        null=False,
        blank=False,
        default=now
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='категория'
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='media/posts/'
    )
    slug = models.SlugField(
        max_length=128,
        unique=True,
        null=False,
        blank=False,
        verbose_name='URL',
        help_text='уникальная ссылка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
