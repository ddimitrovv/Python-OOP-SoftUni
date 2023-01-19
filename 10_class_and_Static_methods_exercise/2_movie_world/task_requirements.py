# Class Customer
# Upon initialization, the Customer class should receive the following parameters:
# name: str, age: int, id: int. Each customer should also have
# an instance attribute called rented_dvds (empty list with DVD instances).
# Implement the __repr__ method, so it returns the following string:
# "{id}: {name} of age {age} has {count_rented_dvds} rented DVDs ({dvd_names joined by comma and space})"

# Class DVD
# Upon initialization, the DVD class should receive the following parameters:
# name: str, id: int, creation_year: int, creation_month: str, age_restriction: int.
# Each DVD should also have an attribute called is_rented (False by default)
# Create a method called from_date(id: int, name: str, date: str, age_restriction: int) -
# it should create a new instance using the provided data. The date will be in the format
# "day.month.year" - all of them should be numbers.
# Implement the __repr__ method, so it returns the following string:
# "{id}: {name} ({creation_month} {creation_year}) has age restriction {age_restriction}. Status: {rented/not rented}"

# Class MovieWorld
# The MovieWorld class should receive one parameter upon initialization:
# name: str. Each MovieWorld instance should also have 2 more attributes:
# customers (empty list of Customer objects), dvds (empty list of DVD objects).
# The class should also have the following methods:
#     • dvd_capacity() - returns 15 - the DVD capacity of a movie world
#     • customer_capacity() - returns 10 - the customer capacity of a movie world
#     • add_customer(customer: Customer) - add the customer if capacity not exceeded
#     • add_dvd(dvd: DVD) - add the DVD if capacity not exceeded
#     • rent_dvd(customer_id: int, dvd_id: int)
#         ◦ If the customer has already rented that DVD return "{customer_name} has already rented {dvd_name}"
#         ◦ If the DVD is rented by someone else, return "DVD is already rented"
#         ◦ If the customer is not allowed to rent the DVD, return:
#           "{customer_name} should be at least {dvd_age_restriction} to rent this movie"
#         ◦ Otherwise, the rent is successful (the DVD is rented and added to the customer's DVDs).
#           Return "{customer_name} has successfully rented {dvd_name}"
#     • return_dvd(customer_id, dvd_id) - if the DVD is in the customer, he/she should return it
#       and the method should return the message "{customer_name} has successfully returned {dvd_name}".
#       Otherwise, return "{customer_name} does not have that DVD"
#     • __repr__() - return the string representation of each customer and each DVD on separate lines
