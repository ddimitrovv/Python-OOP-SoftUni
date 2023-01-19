# You are tasked to create two classes: a Pokemon class in the pokemon.py file
# and a Trainer class in the trainer.py file.
# The Pokemon class should receive a name (string) and health (int) upon initialization.
# It should also have a method called pokemon_details that returns
# the information about the pokemon: "{pokemon_name} with health {pokemon_health}"
# The Trainer class should receive a name (string).
# The Trainer should also have an attribute pokemons (list, empty by default). The Trainer has three methods:
#   - add_pokemon(pokemon: Pokemon)
#       o Adds the pokemon to the collection and returns "Caught {pokemon_name} with health {pokemon_health}".
#           Hint: use the pokemon's details method.
#       o If the pokemon is already in the collection, returns "This pokemon is already caught"
#       o Hint: to import the Pokemon class, you should add "from project1.pokemon import Pokemon"
#   - release_pokemon(pokemon_name: string)
#       o Checks if you have a pokemon with that name and removes it from the collection.
#           In the end, returns "You have released {pokemon_name}"
#       o If there is no pokemon with that name in the collection, returns "Pokemon is not caught"
#   - trainer_data()
#       o The method returns the information about the trainer and his pokemon's collection in the format:
#           "Pokemon Trainer {trainer_name} Pokemon count {the amount of pokemon caught} - {pokemon_details1}
#            ... - {pokemon_detailsN}"

class Pokemon:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f'{self.name} with health {self.health}'
