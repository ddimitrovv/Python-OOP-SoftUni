from unittest import TestCase, main

from project.library import Library


class TestTeam(TestCase):
    LIBRARY_NAME = 'Library'

    def setUp(self) -> None:
        self.library = Library(self.LIBRARY_NAME)

    def test_init__valid_name__expected_correct_result(self):
        self.assertEqual(self.LIBRARY_NAME, self.library.name)
        self.assertDictEqual({}, dict(self.library.books_by_authors))
        self.assertDictEqual({}, dict(self.library.readers))

    def test_init__empty_string_name__expected_to_raise_value_error(self):
        with self.assertRaises(ValueError) as error:
            library = Library('')
        expected = "Name cannot be empty string!"
        self.assertEqual(expected, str(error.exception))

    def test_add_book__author_and_book_not_in_library__expected_to_be_added(self):
        author = "J.K.Rowling"
        book = "Harry Potter and the chamber of secrets"
        self.library.add_book(author, book)
        self.assertDictEqual({author: [book]}, dict(self.library.books_by_authors))

    def test_add_book__author_in_library__expected_book_to_be_added(self):
        author = "J.K.Rowling"
        book = "Harry Potter and the chamber of secrets"
        book2 = "Harry Potter and the goblet of fire"
        self.library.add_book(author, book)
        self.library.add_book(author, book2)
        self.assertDictEqual({author: [book, book2]}, dict(self.library.books_by_authors))

    def test_add_book__book_in_titles__expected_book__not_to_be_added(self):
        author = "J.K.Rowling"
        book = "Harry Potter and the chamber of secrets"
        self.library.add_book(author, book)
        self.library.add_book(author, book)
        self.assertDictEqual({author: [book]}, dict(self.library.books_by_authors))

    def test_add_book__author_and_book_in_library__expected_not_to_be_added(self):
        author = "J.K.Rowling"
        book = "Harry Potter and the chamber of secrets"
        self.library.add_book(author, book)
        self.library.add_book(author, book)
        self.assertDictEqual({author: [book]}, dict(self.library.books_by_authors))

    def test_add_reader__name_not_in_readers__expected_to_be_added(self):
        reader = "Nikodim"
        self.library.add_reader(reader)
        expected = {reader: []}
        self.assertDictEqual(expected, dict(self.library.readers))

    def test_add_reader__name_in_readers__expected_to_return_correct_string(self):
        reader = "Nikodim"
        self.library.add_reader(reader)
        expected = f"{reader} is already registered in the {self.LIBRARY_NAME} library."
        actual = self.library.add_reader(reader)
        self.assertEqual(expected, actual)
        self.assertDictEqual({reader: []}, dict(self.library.readers))

    def test_rent_book__reader_not_in_readers__expected_correct_string(self):
        reader = "Nikodim"
        author = "J.K.Rowling"
        book = "Harry Potter and the chamber of secrets"
        expected = f"{reader} is not registered in the {self.LIBRARY_NAME} Library."
        actual = self.library.rent_book(reader, author, book)
        self.assertEqual(expected, actual)

    def test_rent_book__author_not_in_library__expected_correct_string(self):
        reader = "Nikodim"
        self.library.add_reader(reader)
        author = "J.K.Rowling"
        book = "Harry Potter and the chamber of secrets"
        expected = f"{self.LIBRARY_NAME} Library does not have any {author}'s books."
        actual = self.library.rent_book(reader, author, book)
        self.assertEqual(expected, actual)

    def test_rent_book__book_not_in_library__expected_correct_string(self):
        reader = "Nikodim"
        self.library.add_reader(reader)
        author = "J.K.Rowling"
        book = "Harry Potter and the chamber of secrets"
        book2 = "Harry Potter and the goblet of fire"
        self.library.add_book(author, book)
        expected = f"""{self.LIBRARY_NAME} Library does not have {author}'s "{book2}"."""
        actual = self.library.rent_book(reader, author, book2)
        self.assertEqual(expected, actual)

    def test_rent_book__reader_author_and_book_in_library__expected_correct_string(self):
        reader = "Nikodim"
        self.library.add_reader(reader)
        author = "J.K.Rowling"
        book = "Harry Potter and the chamber of secrets"
        book2 = "Harry Potter and the goblet of fire"
        self.library.add_book(author, book2)
        self.library.add_book(author, book)
        self.library.rent_book(reader, author, book2)
        self.assertDictEqual({reader: [{author: book2}]}, dict(self.library.readers))
        self.assertEqual({author: [book]}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
