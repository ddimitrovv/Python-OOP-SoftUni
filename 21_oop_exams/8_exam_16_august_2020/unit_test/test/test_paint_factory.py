from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory
from project.factory.factory import Factory


class TestPaintFactory(TestCase):
    FACTORY_NAME = 'Paint factory'
    FACTORY_CAPACITY = 1000
    VALID_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]

    def setUp(self) -> None:
        self.paint_factory = PaintFactory(self.FACTORY_NAME, self.FACTORY_CAPACITY)

    def test_init__expected_correct_object(self):
        self.assertEqual(self.FACTORY_NAME, self.paint_factory.name)
        self.assertEqual(self.FACTORY_CAPACITY, self.paint_factory.capacity)
        self.assertDictEqual({}, dict(self.paint_factory.ingredients))
        self.assertListEqual(self.VALID_INGREDIENTS, self.paint_factory.valid_ingredients)

    def test_can_add__value_greater_than_capacity__expected_false(self):
        value = 1001
        self.assertFalse(self.paint_factory.can_add(value))

    def test_can_add__value_less_than_capacity__expected_true(self):
        value = 800
        self.assertTrue(self.paint_factory.can_add(value))

    def test_add_ingredient__product_in_valid_ingredients_can_add__expected_to_be_added(self):
        product_type = 'white'
        quantity = 100
        self.paint_factory.add_ingredient(product_type, quantity)
        self.assertEqual({product_type: quantity}, dict(self.paint_factory.ingredients))

    def test_add_ingredient__product_in_valid_ingredients_cannot_add__expected_to_raise_value_error(self):
        product_type = 'white'
        quantity = 1200
        expected = "Not enough space in factory"
        with self.assertRaises(ValueError) as error:
            self.paint_factory.add_ingredient(product_type, quantity)
        self.assertEqual(expected, str(error.exception))

    def test_add_ingredient__invalid_ingredients__expected_to_raise_type_error(self):
        product_type = 'purple'
        quantity = 100
        expected = f"Ingredient of type {product_type} not allowed in PaintFactory"
        with self.assertRaises(TypeError) as error:
            self.paint_factory.add_ingredient(product_type, quantity)
        self.assertEqual(expected, str(error.exception))

    def test_remove_ingredient__ingredient_in_factory__expected_to_be_removed(self):
        product_type = 'white'
        quantity = 100
        quantity_to_remove = 50
        self.paint_factory.add_ingredient(product_type, quantity)
        self.paint_factory.remove_ingredient(product_type, quantity_to_remove)
        self.assertEqual({product_type: quantity-quantity_to_remove}, dict(self.paint_factory.ingredients))

    def test_remove_ingredient__ingredient_in_factory_higher_quantity__expected_to_raise_value_error(self):
        product_type = 'white'
        quantity = 100
        quantity_to_remove = 200
        expected = "Ingredients quantity cannot be less than zero"
        self.paint_factory.add_ingredient(product_type, quantity)
        with self.assertRaises(ValueError) as error:
            self.paint_factory.remove_ingredient(product_type, quantity_to_remove)
        self.assertEqual(expected, str(error.exception))

    def test_remove_ingredient__ingredient_not_in_factory__expected_to_raise_key_error(self):
        product_type = 'white'
        quantity = 100
        product_to_remove = 'purple'
        quantity_to_remove = 100
        expected = "'No such ingredient in the factory'"
        self.paint_factory.add_ingredient(product_type, quantity)
        with self.assertRaises(KeyError) as error:
            self.paint_factory.remove_ingredient(product_to_remove, quantity_to_remove)
        self.assertEqual(expected, str(error.exception))
        self.assertEqual({product_type: quantity}, dict(self.paint_factory.ingredients))

    def test_repr__without_ingredients__expected_correct_str(self):
        expected = f"Factory name: {self.FACTORY_NAME} with capacity {self.FACTORY_CAPACITY}.\n"
        self.assertEqual(expected, repr(self.paint_factory))

    def test_repr__with_ingredients__expected_correct_str(self):
        product_type = 'white'
        quantity = 100
        product_type2 = 'red'
        quantity2 = 300
        self.paint_factory.add_ingredient(product_type, quantity)
        self.paint_factory.add_ingredient(product_type2, quantity2)
        expected = f"Factory name: {self.FACTORY_NAME} with capacity {self.FACTORY_CAPACITY}.\n"
        expected += f"{product_type}: {quantity}\n"
        expected += f"{product_type2}: {quantity2}\n"
        self.assertEqual(expected, repr(self.paint_factory))

    def test_abstract_class__expected_to_raise_type_error(self):
        name = 'Factory'
        capacity = 100
        with self.assertRaises(TypeError):
            Factory(name, capacity)

    def test_products__without_products__expected(self):
        self.assertEqual({}, dict(self.paint_factory.products))

    def test_products__with_products__expected(self):
        product_type = 'white'
        quantity = 100
        product_type2 = 'red'
        quantity2 = 300
        self.paint_factory.add_ingredient(product_type, quantity)
        self.paint_factory.add_ingredient(product_type2, quantity2)
        self.assertEqual(
            {product_type: quantity, product_type2: quantity2}, dict(self.paint_factory.products))


if __name__ == "__main__":
    main()
