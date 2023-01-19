from unittest import TestCase, main

from project1.vehicle import Vehicle


class TestMammal(TestCase):
    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle_init__should_return_correct_obj(self):

        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_vehicle__drive__raise_exception_when_fuel_not_enough(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_vehicle__drive__expected_fuel_decremental(self):
        distance = 50
        fuel_needed = distance * self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(distance)
        expected = self.FUEL - fuel_needed
        self.assertEqual(expected, self.vehicle.fuel)

    def test_vehicle__drive__expected_fuel_decremental_with_max_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION

        self.vehicle.drive(distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel__expected_exception_if_fuel_is_more_than_capacity(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_refuel__expected_fuel_to_be_increased_with_quantity(self):
        quantity = 20
        self.vehicle.fuel -= quantity
        self.vehicle.refuel(quantity)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_vehicle_str__expected_same_string(self):
        expected_str = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        actual_str = self.vehicle.__str__()
        self.assertEqual(expected_str, actual_str)


if __name__ == "__main__":
    main()
