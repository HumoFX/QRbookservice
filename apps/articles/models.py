import datetime
from django.db import models
from django.utils import timezone

from django.utils.text import slugify


class Categories(models.Model):
    category_name = models.CharField('название категория', max_length=200)

    class Meta:
        verbose_name = 'Категорий'
        verbose_name_plural = 'Катерогии'

    def __str__(self):
        return self.category_name


class Books(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    books_name = models.CharField('название книги', max_length=200)
    author_name = models.CharField('имя автора', max_length=200)
    image = models.ImageField(upload_to='img')
    slug = models.SlugField(max_length=200, blank=True)
    book_url = models.CharField('ссылка книги', max_length=300)
    book_desc = models.TextField('описание', default=' ')
    qr_book = models.ImageField(upload_to='img')
    downloaded = models.IntegerField('количество закачек', default=0)
    pub_date = models.DateTimeField('дата публикации')
    bestseller = models.BooleanField('бестселлер')
    total_downloads = models.IntegerField('общая закачка', default=0)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.books_name



# class Bestsellers(models.Model):
#     bestseller_id = models.ForeignKey(Books, on_delete=models.CASCADE)
#     class Meta:
#         verbose_name = 'Бестселлер'
#         verbose_name_plural = 'Бестселлеры'
#
#     def __str__(self):
#         return self.objects



class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('authors name', max_length=200)
    comment_text = models.CharField('text of comments', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
