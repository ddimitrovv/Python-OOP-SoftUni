# Create a class called Player. Upon initialization, it should receive:
#     • Private attribute name: string
#     • Private attribute sprint: int
#     • Private attribute dribble: int
#     • Private attribute passing: int
#     • Private attribute shooting: int
# You should create property only for the name of the player. The class should also have one additional method:
# Override the __str__() method of the class, so it returns:
# "Player: {name}
# Sprint: {sprint}
# Dribble: {dribble}
# Passing: {passing}
# Shooting: {shooting}"
# Create a class called Team. Upon initialization, it should receive:
#     • Private attribute name: string
#     • Private attribute rating: int
# The class should also have a private instance attribute - players: list -
# empty list upon initialization that will contain all the players (objects)
# The Team class have the following methods:
#     • add_player(player: Player)
#     • If the player is already in the team, return "Player {name} has already joined"
#     • Otherwise, add the player to the team and return "Player {name} joined team {team_name}"
#     • remove_player(player_name: str)
#     • Remove the player and return him
#     • If the player is not in the team, return "Player {player_name} not found"
