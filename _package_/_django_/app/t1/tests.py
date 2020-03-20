from django.test import TestCase

from app.t1.models import Book, Author, BookAuthor


class TestBook(TestCase):

    def setUp(self):
        self.book = Book.objects.create(title='title')
        self.book.save()

    def test_book_info(self):
        print(self.book)

    # def tearDown(self):
    #     self.book.delete()


class TestAuthor(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='title')
        self.book.save()

        self.author = Author.objects.create(name='author')
        self.author.save()

        self.book_author = BookAuthor.objects.create(book=self.book, author=self.author)
        self.book_author.save()
    #
    # def tearDown(self):
    #     self.book.delete()
    #     self.author.delete()
    #     self.book_author.delete()
