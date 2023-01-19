from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    TRAIN_NAME = 'Train'
    CAPACITY = 100
    TRAIN_FULL = "Train is full"
    PASSENGER_EXISTS = "Passenger {} Exists"
    PASSENGER_NOT_FOUND = "Passenger Not Found"
    PASSENGER_ADD = "Added passenger {}"
    PASSENGER_REMOVED = "Removed {}"
    ZERO_CAPACITY = 0

    def setUp(self) -> None:
        self.train = Train(self.TRAIN_NAME, self.CAPACITY)

    def test_init__expected_correct_object(self):
        self.assertEqual(self.TRAIN_NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertListEqual([], list(self.train.passengers))

    def test_add__capacity_equal_to_self_capacity__expecter_to_raise_value_error(self):
        passenger = 'Nikodim'
        passenger2 = 'Stamat'
        self.train.capacity = 1
        self.train.add(passenger)
        with self.assertRaises(ValueError) as error:
            self.train.add(passenger2)
        self.assertEqual(self.TRAIN_FULL, str(error.exception))
        self.assertListEqual([passenger], list(self.train.passengers))

    def test_add__passenger_exist__expected_to_raise_value_error(self):
        passenger = 'Nikodim'
        self.train.add(passenger)
        with self.assertRaises(ValueError) as error:
            self.train.add(passenger)
        expected = self.PASSENGER_EXISTS.format(passenger)
        self.assertEqual(expected, str(error.exception))
        self.assertListEqual([passenger], list(self.train.passengers))

    def test_add__passenger_does_not_exist_train_has_capacity_without_passenger__expected_to_be_added(self):
        passenger = 'Nikodim'
        self.train.add(passenger)
        self.assertListEqual([passenger], list(self.train.passengers))

    def test_add__passenger_does_not_exist_train_has_capacity_with_passenger__expected_to_be_added(self):
        passenger = 'Nikodim'
        passenger2 = 'Stamat'
        self.train.add(passenger)
        self.train.add(passenger2)
        self.assertListEqual([passenger, passenger2], list(self.train.passengers))

    def test_remove__without_passengers_in_train_passenger__expected_to_raise_value_error(self):
        passenger = 'Nikodim'
        with self.assertRaises(ValueError) as error:
            self.train.remove(passenger)
        expected = self.PASSENGER_NOT_FOUND.format(passenger)
        self.assertEqual(expected, str(error.exception))
        self.assertListEqual([], list(self.train.passengers))

    def test_remove__with_passengers_in_train_passenger__expected_to_raise_value_error(self):
        passenger = 'Nikodim'
        passenger2 = 'Stamat'
        self.train.add(passenger2)
        with self.assertRaises(ValueError) as error:
            self.train.remove(passenger)
        expected = self.PASSENGER_NOT_FOUND.format(passenger)
        self.assertEqual(expected, str(error.exception))
        self.assertListEqual([passenger2], list(self.train.passengers))

    def test_remove__with_one_passenger_in_train_passenger__expected_to_be_removed(self):
        passenger = 'Nikodim'
        self.train.add(passenger)
        actual = self.train.remove(passenger)
        expected = self.PASSENGER_REMOVED.format(passenger)
        self.assertEqual(expected, actual)
        self.assertListEqual([], list(self.train.passengers))

    def test_remove__with_some_passengers_in_train_passenger__expected_to_be_removed(self):
        passenger = 'Nikodim'
        passenger2 = 'Stamat'
        self.train.add(passenger)
        self.train.add(passenger2)
        actual = self.train.remove(passenger)
        expected = self.PASSENGER_REMOVED.format(passenger)
        self.assertEqual(expected, actual)
        self.assertListEqual([passenger2], list(self.train.passengers))


if __name__ == '__main__':
    main()
