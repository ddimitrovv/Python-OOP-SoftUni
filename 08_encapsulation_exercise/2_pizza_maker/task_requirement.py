# Create a class called Topping. Upon initialization, it should receive:
#     • topping_type: str - if the topping is an empty string,
#       raise a ValueError with the message "The topping type cannot be an empty string"
#     • weight: float - if the weight is 0 or less,
#       raise a ValueError with the message "The weight cannot be less or equal to zero"
# Hint: Use Getters and Setters.
# Create a class called Dough. Upon initialization, it should receive:
#     • flour_type: str - if the flour type is an empty string,
#       raise a ValueError with the message "The flour type cannot be an empty string"
#     • baking_technique: str - if the technique is an empty string,
#       raise a ValueError with the message "The baking technique cannot be an empty string"
#     • weight: float - if the weight is 0 or less,
#       raise a ValueError with the message "The weight cannot be less or equal to zero"
# Create a class called Pizza. Upon initialization, it should receive:
#     • name: str - if the name is an empty string,
#       raise a ValueError with the message "The name cannot be an empty string"
#     • dough: Dough - if the dough is None,
#       raise a ValueError with the message "You should add dough to the pizza"
#     • toppings_capacity: int – represents the maximum number of toppings the pizza should have.
#       If the capacity is 0 or less,
#           raise a ValueError with the message "The topping's capacity cannot be less or equal to zero"
#     • toppings: dict – empty dictionary upon initialization that will contain
#       the topping type as a key and the topping's weight as a value.
# The class should also have 2 instance methods:
#     • add_topping(topping: Topping)
#         ◦ Add a new topping to the dictionary
#     • If there is no space left for a new topping, raise a ValueError: "Not enough space for another topping"
#     • If the topping is already in the dictionary, increase the value of its weight.
#     • calculate_total_weight() - returns the total weight of the pizza (dough's weight and toppings' weight)
