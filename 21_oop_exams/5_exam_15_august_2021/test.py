from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

bread = Bread('bread ', 1.75)
print(str(bread))
drink = Water('water', 500, 'Gorna Banya')
print(repr(drink))
table = InsideTable(25, 10)
bakery = Bakery("Some Bakery")
print(bakery.add_table('InsideTable', 25, 10))
print(bakery.add_food('Bread', 'some bread', 1.75))
print(bakery.order_food(25, 'Bread'))
print(bakery.reserve_table(8))
table2 = OutsideTable(53, 8)
cake = Cake('cake', 3)
# print(bakery.add_table("InsideTable", 25, 8))
print(bakery.add_food('Cake', 'cake', 1.99))
print(bakery.add_drink('Water', 'some water', 500, 'Gorna Banya'))
print(bakery.order_food(25, 'cake'))
print(bakery.order_food(25, 'cake2'))
print(bakery.order_drink(25, 'some water', 'some juice'))
# print(bakery.order_drink(25, 'some juice'))
print(bakery.add_table('OutsideTable', 52, 20))
print(bakery.get_free_tables_info())
print(bakery.leave_table(25))
print(bakery.get_total_income())
