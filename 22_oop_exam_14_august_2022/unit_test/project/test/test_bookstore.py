from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    BOOK_STORE_LIMIT = 100

    def setUp(self) -> None:
        self.book_store = Bookstore(self.BOOK_STORE_LIMIT)

    def test_init__expected_correct_object(self):
        self.assertEqual(self.BOOK_STORE_LIMIT, self.book_store.books_limit)
        self.assertDictEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_total_sold_books__without_books__expected_zero(self):
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_total_sold_books__with_books__expected_correct_number(self):
        self.assertEqual(0, self.book_store.total_sold_books)
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        book2 = 'Harry Potter and the philosophers stone'
        quantity2 = 20
        self.book_store.receive_book(book, quantity)
        self.book_store.receive_book(book2, quantity2)
        quantity_to_sell = 5
        self.book_store.sell_book(book, quantity_to_sell)
        self.assertEqual(quantity_to_sell, self.book_store.total_sold_books)

    def test_books_limit__value_equal_to_zero__expected_to_raise_value_error(self):
        value = 0
        with self.assertRaises(ValueError) as error:
            self.book_store.books_limit = value
        expected = f"Books limit of {value} is not valid"
        self.assertEqual(expected, str(error.exception))

    def test_books_limit__expected_correct_object(self):
        value = 1
        self.book_store.books_limit = value
        self.assertEqual(value, self.book_store.books_limit)
        self.assertDictEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_books_limit__negative_value__expected_to_raise_value_error(self):
        value = -1
        with self.assertRaises(ValueError) as error:
            self.book_store.books_limit = value
        expected = f"Books limit of {value} is not valid"
        self.assertEqual(expected, str(error.exception))

    def test_books_limit__negative_value_second_test__expected_to_raise_value_error(self):
        value = -10
        with self.assertRaises(ValueError) as error:
            self.book_store.books_limit = value
        expected = f"Books limit of {value} is not valid"
        self.assertEqual(expected, str(error.exception))

    def test_dunder_len__without_books__expected_zero(self):
        actual = self.book_store.__len__()
        self.assertEqual(0, actual)

    def test_dunder_len__with_books__expected_zero(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        book2 = 'Harry Potter and the philosophers stone'
        quantity2 = 20
        self.book_store.availability_in_store_by_book_titles = {
            book: quantity,
            book2: quantity2}
        actual = self.book_store.__len__()
        self.assertEqual(quantity + quantity2, actual)

    def test_receive_book__no_space__expected_to_raise_exception(self):
        self.book_store.books_limit = 5
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        with self.assertRaises(Exception) as error:
            self.book_store.receive_book(book, quantity)
        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(error.exception))
        self.assertDictEqual({}, dict(self.book_store.availability_in_store_by_book_titles))

    def test_receive_book__with_books_no_space__expected_to_raise_exception(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        book2 = 'Harry Potter and the philosophers stone'
        quantity2 = 91
        self.book_store.receive_book(book, quantity)
        with self.assertRaises(Exception) as error:
            self.book_store.receive_book(book2, quantity2)
        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(error.exception))
        self.assertDictEqual({book: quantity}, dict(self.book_store.availability_in_store_by_book_titles))

    def test_receive_book__without_books__expected_to_be_added(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        actual = self.book_store.receive_book(book, quantity)
        self.assertDictEqual({book: quantity}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(quantity, self.book_store.__len__())
        expected = f"{quantity} copies of {book} are available in the bookstore."
        self.assertEqual(expected, actual)
        self.assertDictEqual({book: quantity}, dict(self.book_store.availability_in_store_by_book_titles))

    def test_receive_book__with_books__expected_to_be_added(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        book2 = 'Harry Potter and the philosophers stone'
        quantity2 = 20
        self.book_store.receive_book(book, quantity)
        expected = f"{quantity2} copies of {book2} are available in the bookstore."
        actual = self.book_store.receive_book(book2, quantity2)
        self.assertDictEqual({book: quantity, book2: quantity2}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(quantity + quantity2, self.book_store.__len__())
        self.assertEqual(expected, actual)
        self.assertDictEqual({book: quantity, book2: quantity2},
                             dict(self.book_store.availability_in_store_by_book_titles))

    def test_receive_book__same_book__expected_to_be_added(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        quantity2 = 20
        self.book_store.receive_book(book, quantity)
        expected = f"{quantity + quantity2} copies of {book} are available in the bookstore."
        actual = self.book_store.receive_book(book, quantity2)
        self.assertDictEqual({book: quantity + quantity2}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(quantity + quantity2, self.book_store.__len__())
        self.assertEqual(expected, actual)
        self.assertDictEqual({book: quantity + quantity2},
                             dict(self.book_store.availability_in_store_by_book_titles))

    def test_receive_book__with_books_at_limit__expected_to_be_added(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        book2 = 'Harry Potter and the philosophers stone'
        quantity2 = 90
        self.book_store.receive_book(book, quantity)
        self.book_store.receive_book(book2, quantity2)
        self.assertDictEqual({book: quantity, book2: quantity2},
                             dict(self.book_store.availability_in_store_by_book_titles))
        self.assertEqual(quantity + quantity2, self.book_store.__len__())

    def test_sell_book__without_books__expected_to_raise_exception(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        with self.assertRaises(Exception) as error:
            self.book_store.sell_book(book, quantity)
        expected = f"Book {book} doesn't exist!"
        self.assertEqual(expected, str(error.exception))
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_sell_book_with_books_not_enough_quantity__expected_to_raise_exception(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        self.book_store.receive_book(book, quantity)
        quantity_to_sell = 15
        with self.assertRaises(Exception) as error:
            self.book_store.sell_book(book, quantity_to_sell)
        expected = f"{book} has not enough copies to sell. Left: {quantity}"
        self.assertEqual(expected, str(error.exception))
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_sell_book_with_books_and_enough_quantity__expected_to_be_sold(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 30
        self.book_store.receive_book(book, quantity)
        quantity_to_sell = 15
        actual = self.book_store.sell_book(book, quantity_to_sell)
        expected = f"Sold {quantity_to_sell} copies of {book}"
        self.assertEqual(expected, actual)
        self.assertDictEqual({book: quantity - quantity_to_sell},
                             dict(self.book_store.availability_in_store_by_book_titles))
        self.assertEqual(quantity_to_sell, self.book_store.total_sold_books)

    def test_sell_book_with_books_same_quantity__expected_to_be_sold(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 30
        self.book_store.receive_book(book, quantity)
        quantity_to_sell = 30
        actual = self.book_store.sell_book(book, quantity_to_sell)
        expected = f"Sold {quantity_to_sell} copies of {book}"
        self.assertEqual(expected, actual)
        self.assertDictEqual({book: quantity - quantity_to_sell},
                             dict(self.book_store.availability_in_store_by_book_titles))
        self.assertEqual(quantity_to_sell, self.book_store.total_sold_books)

    def test_dunder_str__without_books__expected_correct_string(self):
        expected = f"""Total sold books: {0}
Current availability: {0}"""
        actual = str(self.book_store)
        self.assertEqual(expected, actual)

    def test_dunder_str__without_sold_books__expected_correct_string(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        book2 = 'Harry Potter and the philosophers stone'
        quantity2 = 20
        self.book_store.receive_book(book, quantity)
        self.book_store.receive_book(book2, quantity2)
        expected = f"""Total sold books: {0}
Current availability: {quantity + quantity2}
 - {book}: {quantity} copies
 - {book2}: {quantity2} copies"""
        actual = str(self.book_store)
        self.assertEqual(expected, actual)

    def test_dunder_str__with_sold_books__expected_correct_string(self):
        book = 'Harry Potter and the goblet of fire'
        quantity = 10
        book2 = 'Harry Potter and the philosophers stone'
        quantity2 = 20
        self.book_store.receive_book(book, quantity)
        self.book_store.receive_book(book2, quantity2)
        quantity_to_sell = 5
        self.book_store.sell_book(book, quantity_to_sell)
        expected = f"""Total sold books: {quantity_to_sell}
Current availability: {(quantity + quantity2) - quantity_to_sell}
 - {book}: {quantity - quantity_to_sell} copies
 - {book2}: {quantity2} copies"""
        actual = str(self.book_store)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
