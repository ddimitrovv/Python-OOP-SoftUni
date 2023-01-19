from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    SHOP_NAME = 'Pet shop'

    def setUp(self) -> None:
        self.pet_shop = PetShop(self.SHOP_NAME)

    def test_init__expected_correct_object(self):
        self.assertEqual(self.SHOP_NAME, self.pet_shop.name)
        self.assertDictEqual({}, dict(self.pet_shop.pets))
        self.assertListEqual([], list(self.pet_shop.pets))

    def test_add_food__quantity_less_than_zero__expecter_to_raise_value_error(self):
        food_name = 'Max animal'
        quantity = -5
        expected = 'Quantity cannot be equal to or less than 0'
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food(food_name, quantity)
        self.assertEqual(expected, str(error.exception))

    def test_add_food__quantity_equal_to_zero__expecter_to_raise_value_error(self):
        food_name = 'Max animal'
        quantity = 0
        expected = 'Quantity cannot be equal to or less than 0'
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food(food_name, quantity)
        self.assertEqual(expected, str(error.exception))

    def test_add_food__food_name_not_in_dict__expected_to_be_added(self):
        food_name = 'Max animal'
        quantity = 1000
        expected = f"Successfully added {quantity:.2f} grams of {food_name}."
        actual = self.pet_shop.add_food(food_name, quantity)
        self.assertEqual(expected, actual)
        self.assertDictEqual({food_name: quantity}, dict(self.pet_shop.food))

    def test_add_food__food_name_in_dict__expected_quantity_to_be_increased(self):
        food_name = 'Max animal'
        quantity = 1000
        expected = f"Successfully added {quantity:.2f} grams of {food_name}."
        self.pet_shop.add_food(food_name, quantity)
        actual = self.pet_shop.add_food(food_name, quantity)
        self.assertEqual(expected, actual)
        self.assertDictEqual({food_name: quantity + quantity}, dict(self.pet_shop.food))

    def test_add_pet__pet_not_in_pets__expected_to_be_added(self):
        pet = "Rex"
        actual = self.pet_shop.add_pet(pet)
        expected = f"Successfully added {pet}."
        self.assertEqual(expected, actual)
        self.assertListEqual([pet], list(self.pet_shop.pets))

    def test_add_pet__pet_in_pets__expected_to_raise_exception(self):
        pet = "Rex"
        self.pet_shop.add_pet(pet)
        with self.assertRaises(Exception) as error:
            self.pet_shop.add_pet(pet)
        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(error.exception))

    def test_feed_pet__pet_not_in_pets__expected_to_raise_exception(self):
        pet = "Rex"
        food_name = 'Max animal'
        quantity = 1000
        self.pet_shop.add_food(food_name, quantity)
        with self.assertRaises(Exception) as error:
            self.pet_shop.feed_pet(food_name, pet)
        expected = f"Please insert a valid pet name"
        self.assertEqual(expected, str(error.exception))

    def test_feed_pet__food_not_in_shop__expected_correct_string(self):
        pet = "Rex"
        food_name = 'Max animal'
        self.pet_shop.add_pet(pet)
        actual = self.pet_shop.feed_pet(food_name, pet)
        expected = f'You do not have {food_name}'
        self.assertEqual(expected, actual)

    def test_feed_pet__food_not_enough__expected_correct_string_and_to_ad_food(self):
        pet = "Rex"
        food_name = 'Max animal'
        quantity = 50
        self.pet_shop.add_pet(pet)
        self.pet_shop.add_food(food_name, quantity)
        actual = self.pet_shop.feed_pet(food_name, pet)
        expected = "Adding food..."
        self.assertEqual(expected, actual)
        self.assertDictEqual({food_name: quantity + 1000.00}, dict(self.pet_shop.food))

    def test_feed_pet__food_enough__expected_pet_to_be_fed(self):
        pet = "Rex"
        food_name = 'Max animal'
        quantity = 1000
        self.pet_shop.add_pet(pet)
        self.pet_shop.add_food(food_name, quantity)
        actual = self.pet_shop.feed_pet(food_name, pet)
        expected = f"{pet} was successfully fed"
        self.assertEqual(expected, actual)
        self.assertDictEqual({food_name: quantity - 100}, dict(self.pet_shop.food))

    def test_repr_with_pets__expected_correct_string(self):
        pets = ["Rex", "Tom", "Jerry"]
        for pet in pets:
            self.pet_shop.add_pet(pet)
        expected = f'Shop {self.SHOP_NAME}:\n' \
                   f'Pets: {", ".join(pets)}'
        actual = repr(self.pet_shop)
        self.assertEqual(expected, actual)

    def test_repr_without_pets__expected_correct_string(self):
        pets = []
        expected = f'Shop {self.SHOP_NAME}:\n' \
                   f'Pets: {", ".join(pets)}'
        actual = repr(self.pet_shop)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
