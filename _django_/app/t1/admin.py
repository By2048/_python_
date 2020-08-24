from django.contrib import admin

from app.t1.models import Book, Author, BookAuthor


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = list_display


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = list_display
