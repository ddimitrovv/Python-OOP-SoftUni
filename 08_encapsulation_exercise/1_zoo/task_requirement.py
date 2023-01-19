# The Animal class is a base class for any type of animal in the zoo.
# It should receive four public attributes - a name (string), a gender (str), an age (int),
# and a money_for_care (int) upon initialization.
# The Animal class should also have 1 additional method:
#     • __repr__() - returns string representation of the animal in the format:
#       "Name: {name}, Age: {age}, Gender: {gender}"
# The Lion, the Tiger, and the Cheetah classes should inherit from the Animal class.
# Each of these animals costs a certain amount of money to be cared for:
#     • A lion needs 50
#     • A tiger needs 45
#     • A cheetah needs 60
# The Worker class is a base class for any type of employee in the zoo.
# It should receive three public attributes - a name (string), an age (int), and a salary (int)
# upon initialization.
# The Worker class should also have one method:
#     • __repr__() - returns string representation of the workers in the format:
#       "Name: {name}, Age: {age}, Salary: {salary}"
# The Keeper, the Caretaker, and the Vet classes should inherit from the Worker class.
# The Zoo class should receive 4 attributes upon initialization:
#     • Public attribute name: string
#     • Private attribute budget: int
#     • Private attribute animal_capacity: int
#     • Private attribute workers_capacity: int
# It should also have 2 instance attributes:
#     • Public attribute animals: list - (empty upon initialization)
#     • Public attribute workers: list - (empty upon initialization)
# The Zoo class should also have 8 methods:
#     • add_animal(animal, price)
#     • If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah)
#       to the animals' list, reduce the budget,
#       and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
#     • If you have the capacity, but no budget, return "Not enough budget"
#     • In any other case, you do not have space, and you should return "Not enough space for animal"
#     • hire_worker(worker)
#     • If you have not exceeded the capacity of workers in the zoo for the worker
#       (instance of Keeper/Caretaker/Vet), add him to the workers
#       and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
#     • Otherwise, return "Not enough space for worker"
#     • fire_worker(worker_name)
#     • If there is a worker with that name in the workers' list,
#       remove him and return "{worker_name} fired successfully"
#     • Otherwise, return "There is no {worker_name} in the zoo"
#     • pay_workers()
#     • If you have enough budget to pay the workers (sum their salaries) pay them
#       and return "You payed your workers. They are happy. Budget left: {left_budget}"
#     • Otherwise, return "You have no budget to pay your workers. They are unhappy"
#     • tend_animals()
#     • If you have enough budget to take care of the animals, reduce the budget and
#       return "You tended all the animals. They are happy. Budget left: {left_budget}"
#     • Otherwise, return "You have no budget to tend the animals. They are unhappy."
#     • profit(amount)
#     • Increase the budget with the given amount of profit
#     • animals_status()
#         ◦ Returns the following string (Hint: use the __repr__ methods of the animals to print them on the console):
# "You have {total_animals_count} animals
# ----- {amount_of_lions} Lions:
# {lion1}
# …
# {lionN}
# ----- {amount_of_tigers} Tigers:
# {tiger1}
# …
# {tigerN}
# ----- {amount_of_cheetahs} Cheetahs:
# {cheetah1}
# …
# {cheetahN}"
#     • workers_status()
#         ◦ Returns the following string (Hint: use the __repr__ methods of the workers to print them on the console):
# "You have {total_workers_count} workers
# ----- {amount_of_keepers} Keepers:
# {keeper1}
# …
# {keeperN}
# ----- {amount_of_caretakers} Caretakers:
# {caretaker1}
# …
# {caretakerN}
# ----- {amount_of_vets} Vets:
# {vet1}
# …
# {vetN}"
