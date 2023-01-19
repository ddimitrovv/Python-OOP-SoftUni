import os

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.validators import name_validator, if_item_name_exists


class Bakery:
    NAME_ERROR_MESSAGE = "Name cannot be empty string or white space!"
    food_types = {
        'Bread': Bread,
        'Cake': Cake,
    }
    drink_types = {
        'Tea': Tea,
        'Water': Water,
    }
    table_types = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable,
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in self.food_types:
            return
        if if_item_name_exists(name, self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")
        food = self.food_types[food_type](name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in self.drink_types:
            return
        if if_item_name_exists(name, self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        drink = self.drink_types[drink_type](name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in self.table_types:
            return
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")
        table = self.table_types[table_type](table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved:
                table.reserve(number_of_people)
                if table.is_reserved:
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        food_could_be_ordered = []
        ordered_food_by_name = []
        for item in args:
            for food in self.food_menu:
                if item == food.name:
                    food_could_be_ordered.append(food)
                    ordered_food_by_name.append(food.name)
                    table[0].order_food(food)
                    break
        not_ordered_food = [f for f in args if f not in ordered_food_by_name]

        output = f"Table {table_number} ordered:" + os.linesep
        for food in food_could_be_ordered:
            output += repr(food) + os.linesep
        output += f"{self.name} does not have in the menu:" + os.linesep
        for food in not_ordered_food:
            output += food + os.linesep
        return output.strip()

    def order_drink(self, table_number: int, *args):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        drinks_could_be_ordered = []
        ordered_drinks_by_name = []
        for item in args:
            for drink in self.drinks_menu:
                if item == drink.name:
                    drinks_could_be_ordered.append(drink)
                    ordered_drinks_by_name.append(drink.name)
                    table[0].order_drink(drink)
                    break
        not_ordered_drinks = [d for d in args if d not in ordered_drinks_by_name]

        output = f"Table {table_number} ordered:" + os.linesep
        for drink in drinks_could_be_ordered:
            output += repr(drink) + os.linesep
        output += f"{self.name} does not have in the menu:" + os.linesep
        for drink in not_ordered_drinks:
            output += drink + os.linesep
        return output.strip()

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return
        bill = table[0].get_bill()
        self.total_income += bill
        table[0].clear()
        return f"Table: {table[0].table_number}" + os.linesep + f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        output = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                output += table.free_table_info() + os.linesep
        return output.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
