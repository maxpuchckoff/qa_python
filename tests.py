from main import BooksCollector

class TestBooksCollector:
    def test_books_rating_true(self):
        collector = BooksCollector()
        assert collector.books_rating == {}

    def test_favourites_true(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_new_book_rating_is_one(self):
        collector = BooksCollector()
        collector.add_new_book('Sapiens:краткая история человечества')
        assert collector.books_rating['Sapiens:краткая история человечества'] == 1

    def test_add_new_book_add_the_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Sapiens:краткая история человечества')
        collector.add_new_book('Sapiens:краткая история человечества')
        assert len(collector.get_books_rating()) == 1
    def test_set_book_rating_set_rating_to_book_not_in_list(self):
        collector = BooksCollector()
        collector.set_book_rating('Переписка Энгельса с Каутским', 2)
        assert collector.get_book_rating('Переписка Энгельса с Каутским') == None

    def test_set_book_rating_set_book_rating_less_1(self):
        collector = BooksCollector()
        collector.add_new_book('Переписка Энгельса с Каутским')
        collector.set_book_rating('Переписка Энгельса с Каутским', 0)
        assert collector.get_book_rating('Переписка Энгельса с Каутским') > 0

    def test_set_book_rating_set_book_rating_more_10(self):
        collector = BooksCollector()
        collector.add_new_book('Sapiens:краткая история человечества')
        collector.set_book_rating('Sapiens:краткая история человечества', 15)
        assert collector.get_book_rating('Sapiens:краткая история человечества') < 11

    def test_get_book_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        assert collector.get_book_rating('Тестирование Дот Ком') == 1

    def test_get_books_with_specific_rating_true(self):
        collector = BooksCollector()
        collector.books_rating = {'Мастер и Маргарита': 8, 'Sapiens:краткая история человечества': 8,
                                  'Переписка Энегельса с Каутским': 2}
        assert collector.get_books_with_specific_rating(8) == ['Мастер и Маргарита',
                                                               'Sapiens:краткая история человечества']

    def test_get_books_rating_true(self):
        collector = BooksCollector()
        collector.books_rating = {'Мастер и Маргарита': 8, 'Sapiens:краткая история человечества': 8,
                                  'Переписка Энегельса с Каутским': 2}
        assert collector.get_books_rating() == {'Мастер и Маргарита': 8, 'Sapiens:краткая история человечества': 8,
                                  'Переписка Энегельса с Каутским': 2}

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.books_rating = {'Сага о ведьмаке': 10}
        collector.add_book_in_favorites('Сага о ведьмаке')
        assert collector.favorites == ['Сага о ведьмаке']

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.favorites = ['Сага о ведьмаке', 'Переписка Энгельса с Каутским']
        collector.delete_book_from_favorites('Переписка Энгельса с Каутским')
        assert collector.favorites == ['Сага о ведьмаке']

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.favorites = ['Сага о ведьмаке', 'Переписка Энгельса с Каутским']
        assert collector.get_list_of_favorites_books() == ['Сага о ведьмаке', 'Переписка Энгельса с Каутским']




