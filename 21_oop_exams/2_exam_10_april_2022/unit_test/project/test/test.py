from unittest import TestCase, main

from project.movie import Movie


class TestTeam(TestCase):
    NAME = 'Man in black'
    YEAR = 2000
    RATING = 10
    MIN_YEAR = 1887

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_movie_init__expected_correct_obj(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter__expected_raise_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_year_setter__expected_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = self.MIN_YEAR - 1
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor__actor_not_in_actors__expected_to_be_added(self):
        actor = "Will Smith"
        self.movie.add_actor(actor)
        self.assertEqual([actor], self.movie.actors)

    def test_add_actor__actor_in_actors__expected_correct_str(self):
        actor = "Will Smith"
        self.movie.add_actor(actor)
        expected = f"{actor} is already added in the list of actors!"
        actual = self.movie.add_actor(actor)
        self.assertEqual(expected, actual)

    def test_dt_expected_correct_string(self):
        other_movie = Movie('Matrix', 1999, 9)
        expected = f'"{self.movie.name}" is better than "{other_movie.name}"'
        actual = self.movie > other_movie
        self.assertEqual(expected, actual)
        actual = other_movie > self.movie
        self.assertEqual(expected, actual)

    def test_movie_repr__expected_correct_string(self):
        actor = "Will Smith"
        actor2 = "The Dog"
        self.movie.add_actor(actor)
        self.movie.add_actor(actor2)
        expected = f"Name: {self.movie.name}\n" \
                   f"Year of Release: {self.movie.year}\n" \
                   f"Rating: {self.movie.rating:.2f}\n" \
                   f"Cast: {', '.join(self.movie.actors)}"
        actual = self.movie.__repr__()
        self.assertEqual(expected, actual)
        self.assertEqual([actor, actor2], self.movie.actors)


if __name__ == "__main__":
    main()
