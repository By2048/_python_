from datetime import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = 'db_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, through='BookAuthor')

    class Meta:
        db_table = 'db_author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'db_book_author'
        verbose_name = '图书-作者'
        verbose_name_plural = verbose_name
