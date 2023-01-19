import os

from project.player import Player


class Controller:
    def __init__(self):
        self.players = list()
        self.supplies = list()

    def add_player(self, *players):
        players_to_add = [player for player in players if player not in self.players]
        self.players.extend(players_to_add)
        return f"Successfully added: {', '.join(player.name for player in players_to_add)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        current_player = self.__get_player_by_name(player_name)
        if current_player is None:
            return
        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        sustenance, index = self.__get_sustain(sustenance_type)

        if sustenance is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not current_player.need_sustenance:
            return f"{player_name} have enough stamina."

        current_player.stamina = min((current_player.stamina + sustenance.energy), Player.MAX_STAMINA)
        self.supplies.pop(index)
        return f"{player_name} sustained successfully with {sustenance.name}."

    def __get_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __get_sustain(self, s_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            sustain = self.supplies[idx]
            if sustain.__class__.__name__ == s_type:
                return sustain, idx
        return None, None

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__get_player_by_name(first_player_name)
        second_player = self.__get_player_by_name(second_player_name)
        player_cannot_duel = list()
        if first_player.stamina <= Player.MIN_STAMINA:
            player_cannot_duel.append(f"Player {first_player_name} does not have enough stamina.")
        if second_player.stamina <= Player.MIN_STAMINA:
            player_cannot_duel.append(f"Player {second_player_name} does not have enough stamina.")
        if player_cannot_duel:
            return os.linesep.join(player_cannot_duel)

        if first_player.stamina > second_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_player_damage, Player.MIN_STAMINA)
        if second_player.stamina == 0:
            return f"Winner: {first_player.name}"
        second_player_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_player_damage, Player.MIN_STAMINA)
        if first_player.stamina == 0:
            return f"Winner: {second_player.name}"
        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        # output = [f'{str(player)}' for player in self.players]
        # output += [f'{supply.details()}' for supply in self.supplies]
        # return os.linesep.join(output)
        return os.linesep.join([str(p) for p in self.players]) + os.linesep +\
               os.linesep.join(s.details() for s in self.supplies)
