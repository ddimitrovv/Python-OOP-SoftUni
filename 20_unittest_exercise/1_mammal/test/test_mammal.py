from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.name = "Rex"
        self.mammal_type = "dog"
        self.sound = "woof"
        self.mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_mammal_init__should_return_correct_obj(self):

        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.mammal_type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound__should_return_correct_string(self):
        expected_string = f"{self.mammal.name} makes {self.mammal.sound}"
        self.assertEqual(self.mammal.make_sound(), expected_string)

    def test_get_kingdom__should_return_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info__should_return_correct_string(self):
        expected_string = f"{self.mammal.name} is of type {self.mammal.type}"
        self.assertEqual(self.mammal.info(), expected_string)


if __name__ == "__main__":
    main()
